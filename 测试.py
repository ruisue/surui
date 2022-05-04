import joblib
import pandas as pd
from sklearn.metrics import roc_curve,auc
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold


#定义n折交叉验证
KF = StratifiedKFold(n_splits = 5)
from sklearn.metrics import roc_curve,auc
from scipy import interp
tprs=[]
aucs=[]
mean_fpr=np.linspace(0,1,100)
i=0
#data为数据集,利用KF.split划分训练集和测试集
for train_index,test_index in KF.split(data):
    #建立模型，并对训练集进行测试，求出预测得分
    #划分训练集和测试集
    X_train,X_test = data[train_index],data[test_index]
    Y_train,Y_test = label[train_index],label[test_index]
    #建立模型(模型已经定义)
    model = build_model()
    #编译模型
    model.compile(optimizer = 'sgd',loss = 'categorical_crossentropy',metrics = ['acc'])
    #训练模型
    model.fit(X_train,Y_train,batch_size = 2,validation_data = (X_test,Y_test),epochs = 150)
    #利用model.predict获取测试集的预测值
    y_pred = model.predict(X_test,batch_size = 1)
    #计算fpr(假阳性率),tpr(真阳性率),thresholds(阈值)[绘制ROC曲线要用到这几个值]
    fpr,tpr,thresholds=roc_curve(Y_test[:,1],y_pred[:,1])
    #interp:插值 把结果添加到tprs列表中
    tprs.append(interp(mean_fpr,fpr,tpr))
    tprs[-1][0]=0.0
    #计算auc
    roc_auc=auc(fpr,tpr)
    aucs.append(roc_auc)
    #画图，只需要plt.plot(fpr,tpr),变量roc_auc只是记录auc的值，通过auc()函数计算出来
    plt.plot(fpr,tpr,lw=1,alpha=0.3,label='ROC fold %d(area=%0.2f)'% (i,roc_auc))
    i +=1
#画对角线
plt.plot([0,1],[0,1],linestyle='--',lw=2,color='r',label='Luck',alpha=.8)
mean_tpr=np.mean(tprs,axis=0)
mean_tpr[-1]=1.0
mean_auc=auc(mean_fpr,mean_tpr)#计算平均AUC值
std_auc=np.std(tprs,axis=0)
plt.plot(mean_fpr,mean_tpr,color='b',label=r'Mean ROC (area=%0.2f)'%mean_auc,lw=2,alpha=.8)
std_tpr=np.std(tprs,axis=0)
tprs_upper=np.minimum(mean_tpr+std_tpr,1)
tprs_lower=np.maximum(mean_tpr-std_tpr,0)
plt.fill_between(mean_tpr,tprs_lower,tprs_upper,color='gray',alpha=.2)
plt.xlim([-0.05,1.05])
plt.ylim([-0.05,1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC')
plt.legend(loc='lower right')
plt.show()
