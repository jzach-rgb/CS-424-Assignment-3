import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("results_answers.csv", encoding='cp1252')



main_ids = {f'P{i:02d}' for i in range(1,11)}
study = df[df['participant_id'].isin(main_ids)].copy()
study['accuracy_0_or_1'] = pd.to_numeric(study['accuracy_0_or_1'], errors='raise')
study['time_seconds'] = pd.to_numeric(study['time_seconds'], errors='raise')
study['timed_out_0_or_1'] = pd.to_numeric(study['timed_out_0_or_1'], errors='raise')




summary = study.groupby('condition').agg(
    n=('accuracy_0_or_1','size'), correct=('accuracy_0_or_1','sum'),
    accuracy_pct=('accuracy_0_or_1', lambda s: 100*s.mean()),
    mean_seconds=('time_seconds','mean'), median_seconds=('time_seconds','median'),
    std_seconds=('time_seconds','std'), timeouts=('timed_out_0_or_1','sum')
).reindex(['Static','Interactive'])
by_task = study.groupby(['condition','task_type']).agg(
    n=('accuracy_0_or_1','size'),correct=('accuracy_0_or_1','sum'),
    accuracy_pct=('accuracy_0_or_1',lambda s: 100*s.mean()),mean_seconds=('time_seconds','mean')
)
by_variant = study.groupby(['condition','task_type','variant']).agg(
    n=('accuracy_0_or_1','size'), accuracy_pct=('accuracy_0_or_1',lambda s:100*s.mean()),mean_seconds=('time_seconds','mean')
)
by_order = study.groupby(['condition_order','condition']).agg(
    n=('accuracy_0_or_1','size'),accuracy_pct=('accuracy_0_or_1',lambda s:100*s.mean()),mean_seconds=('time_seconds','mean')
)
participant = study.groupby(['participant_id','condition']).agg(
    accuracy_pct=('accuracy_0_or_1',lambda s:100*s.mean()),mean_seconds=('time_seconds','mean')
).unstack('condition')
summary.to_csv('task4_condition_summary.csv')
by_task.to_csv('task4_by_task.csv')
by_variant.to_csv('task4_by_variant.csv')
by_order.to_csv('task4_by_order.csv')
participant.to_csv('task4_by_participant.csv')

plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
colors=['#777c86','#397fb0']
fig,ax=plt.subplots(figsize=(7,4.6))
bars=ax.bar(summary.index, summary['accuracy_pct'],color=colors,width=.56)
ax.set_ylim(0,105);ax.set_ylabel('Correct responses (%)');ax.set_title('Task accuracy by visualization condition',pad=12)
for bar,v,c,n in zip(bars,summary['accuracy_pct'],summary['correct'],summary['n']):
    ax.text(bar.get_x()+bar.get_width()/2,v+2,f'{v:.0f}% ({int(c)}/{int(n)})',ha='center',fontsize=11)
fig.tight_layout();fig.savefig('task4_accuracy.png',dpi=180);plt.close(fig)

fig,ax=plt.subplots(figsize=(7,4.6))
bars=ax.bar(summary.index,summary['mean_seconds'],color=colors,width=.56)
ax.set_ylim(0,30);ax.set_ylabel('Mean completion time (seconds)');ax.set_title('Completion time by visualization condition',pad=12)
for bar,v in zip(bars,summary['mean_seconds']):
    ax.text(bar.get_x()+bar.get_width()/2,v+.5,f'{v:.2f}s',ha='center',fontsize=11)
ax.text(.5,-.20,'Includes a 90-second timeout in the interactive condition',ha='center',transform=ax.transAxes,fontsize=9)
fig.subplots_adjust(bottom=.24);fig.savefig('task4_completion_time.png',dpi=180);plt.close(fig)

fig,ax=plt.subplots(figsize=(9,4.9))
pt=participant['mean_seconds']
for pid,r in pt.iterrows():
    ax.plot([0,1],[r['Static'],r['Interactive']],marker='o',alpha=.65,linewidth=1.5)
    ax.annotate(pid,(1,r['Interactive']),xytext=(6,0),textcoords='offset points',fontsize=9)
ax.set_xticks([0,1],['Static','Interactive']);ax.set_xlim(-.15,1.28)
ax.set_ylabel('Mean task time (seconds)');ax.set_title('Paired participant completion times',pad=12)
fig.tight_layout();fig.savefig('task4_participants.png',dpi=180);plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(10,4.5))
for k,(metric,ylabel) in enumerate([('accuracy_pct','Accuracy (%)'),('mean_seconds','Mean time (s)')]):
    ax=axes[k]
    tasks=['change','aggregation'];x=np.arange(len(tasks));w=.34
    for i,condition in enumerate(['Static','Interactive']):
        vals=[by_task.loc[(condition,task),metric] for task in tasks]
        bars=ax.bar(x+(i-.5)*w,vals,w,color=colors[i],label=condition)
        for b,v in zip(bars,vals):
            ax.text(b.get_x()+b.get_width()/2,b.get_height()+(.8 if k else 1),f'{v:.1f}',ha='center',fontsize=9)
    ax.set_xticks(x,['Change','Aggregation']);ax.set_ylabel(ylabel)
    ax.set_ylim(0,110 if k==0 else 31)
axes[0].legend(frameon=False);fig.suptitle('Performance differs by analytical task',fontsize=13)
fig.tight_layout();fig.savefig('task4_by_task.png',dpi=180);plt.close(fig)

print('\nCONDITION SUMMARY\n',summary.round(2).to_string())
print('\nBY TASK\n',by_task.round(2).to_string())
print('\nBY ORDER\n',by_order.round(2).to_string())
