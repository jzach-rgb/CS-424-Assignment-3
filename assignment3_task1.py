from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

DRINKS = ['Latte', 'Matcha Latte', 'Chai Latte']
PERIODS = ['9–10 AM', '11 AM–12 PM', '1–3 PM']
HOURS = [f'{h}:00' for h in range(9, 16)]
MIN_N = 8

sales = pd.read_csv("clean_data.csv")


if sales['Is_Drink'].dtype == object:
    is_drink = sales['Is_Drink'].astype(str).str.lower().eq('true')
else:
    is_drink = sales['Is_Drink'].eq(True)
sales['Hour'] = pd.to_numeric(sales['Hour'], errors='coerce')
d = sales.loc[is_drink & sales['Item'].isin(DRINKS)
              & sales['Milk'].notna() & sales['Hour'].between(9, 15)].copy()
d['Hour_Label'] = d['Hour'].astype(int).astype(str) + ':00'
d['Period'] = pd.cut(d['Hour'], bins=[8, 10, 12, 15], labels=PERIODS)


def summarize(column, labels):
    g = d.groupby(['Item', column], observed=True)['Milk'].agg(
        n='size', oat=lambda x: x.eq('Oat').sum())
    g['pct'] = 100 * g['oat'] / g['n']
    index = pd.MultiIndex.from_product(
        [DRINKS, labels], names=['Item', column])
    g = g.reindex(index)
    pct = g['pct'].unstack(column).reindex(index=DRINKS, columns=labels)
    n = g['n'].unstack(column).reindex(index=DRINKS, columns=labels)
    shown = pct.where(n >= MIN_N)
    labels_matrix = []
    for drink in DRINKS:
        row = []
        for label in labels:
            count, value = n.loc[drink, label], shown.loc[drink, label]
            if pd.isna(count):
                row.append('No data')
            elif pd.isna(value):
                row.append(f'n={int(count)}<br>&lt;8 records')
            else:
                row.append(f'{value:.0f}%<br>n={int(count)}')
        labels_matrix.append(row)
    return shown, n, labels_matrix


hourly = summarize('Hour_Label', HOURS)
grouped = summarize('Period', PERIODS)

fig, axes = plt.subplots(2, 1, figsize=(12, 8), constrained_layout=True)
cmap = plt.get_cmap('YlGnBu').copy()
cmap.set_bad('#e5e5e5')
for ax, (pct, n, labels_matrix), labels, title in zip(
        axes, [hourly, grouped], [HOURS, PERIODS],
        ['Hourly oat milk share', 'Grouped-time oat milk share']):
    im = ax.imshow(np.ma.masked_invalid(pct.to_numpy(dtype=float)),
                   cmap=cmap, vmin=0, vmax=80, aspect='auto')
    ax.set_xticks(range(len(labels)), labels)
    ax.set_yticks(range(len(DRINKS)), DRINKS)
    ax.set_title(title)
    for i in range(len(DRINKS)):
        for j in range(len(labels)):
            value = pct.iloc[i, j]
            ax.text(j, i, labels_matrix[i][j].replace('<br>', '\n').replace('&lt;', '<'),
                    ha='center', va='center', fontsize=8,
                    color='white' if pd.notna(value) and value > 45 else 'black')
fig.colorbar(im, ax=axes, label='% oat among recorded milk types', shrink=0.75)
fig.savefig('static_heatmaps.png', dpi=180)
plt.close(fig)


def plot_args(summary, xlabels):
    pct, n, labels_matrix = summary
    return dict(z=pct.to_numpy(dtype=float).tolist(), x=xlabels,
                text=labels_matrix)


h = plot_args(hourly, HOURS)
g = plot_args(grouped, PERIODS)
chart = go.Figure(go.Heatmap(
    z=g['z'], x=g['x'], y=DRINKS, text=g['text'],
    texttemplate='%{text}', textfont={'size': 13},
    colorscale='YlGnBu', zmin=0, zmax=80,
    colorbar={'title': '% oat'},
    hovertemplate='%{y} | %{x}<br>%{text}<extra></extra>',
    hoverongaps=False))
chart.update_layout(
    title='Oat milk preference by drink and time',
    xaxis_title='Time period', yaxis_title='Drink',
    height=480, width=900, margin={'t': 110},
    updatemenus=[{'type': 'dropdown', 'direction': 'down',
                  'x': 0.02, 'y': 1.18, 'showactive': True,
                  'buttons': [
                      {'label': 'Grouped time', 'method': 'update',
                       'args': [{'z': [g['z']], 'x': [g['x']], 'text': [g['text']]},
                                {'xaxis.title.text': 'Time period'}]},
                      {'label': 'Individual hours', 'method': 'update',
                       'args': [{'z': [h['z']], 'x': [h['x']], 'text': [h['text']]},
                                {'xaxis.title.text': 'Hour of day'}]}
                  ]}])
chart.write_html('interactive_heatmap.html', include_plotlyjs=True)
print('Created:', 'static_heatmaps.png')
print('Created:', 'interactive_heatmap.html')
