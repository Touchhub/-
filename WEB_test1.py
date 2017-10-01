from  sklearn import svm
from  sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
path=r'C:\Users\Shinelon\Desktop\train.txt'
data=pd.read_excel(r'C:\Users\Shinelon\Desktop\冶金144班_毕业生资格审查稿2017.9.8.xlsx')
x_data=data.loc[:,['sin_data','cos_data']]
y_data=data.ix[:,'label_data']
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,random_state=1,train_size=0.6)
# print(x_train,y_train)
clf=svm.SVC(C=0.2,kernel='rbf',decision_function_shape='ovr')
clf.fit(x_train,y_train)
print(clf.score(x_train,y_train))
y_hat=clf.predict(x_train)
#print(y_hat)
print(clf.score(x_test,y_test))
y_hat=clf.predict(x_test)
### 以上训练模型完毕  下面确定坐标轴范围
x1_min,x1_max=x_data.loc[:,'sin_data'].min(),x_data.loc[:,'sin_data'].max() #第0列的范围
#print(x1_min,x1_max)
x2_min,x2_max=x_data.loc[:,'cos_data'].min(),x_data.loc[:,'cos_data'].max() #第一列的范围
#print(x1_min,x1_max,x2_min,x2_max)
X1,X2=np.mgrid[x1_min:x1_max:200j,x2_min:x2_max:200j] #生成网格采样点
grid_test=np.stack((X1.flat,X2.flat),axis=1)
grid_hat=clf.predict(grid_test)
grid_hat=grid_hat.reshape(X1.shape)
#print(grid_test)
# 下面开始作图
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.figure()
mpl.rcParams['font.sans-serif']=[u'SimHei']
mpl.rcParams['axes.unicode_minus']=False   #指定默认字体
# 开始绘制
cm_light=mpl.colors.ListedColormap(['#A0FFA0','#FFA0A0','#A0A0FF'])
cm_dark=mpl.colors.ListedColormap(['g','r','b'])
plt.pcolormesh(X1,X2,grid_hat,cmap=cm_light)
plt.scatter(x_data.loc[:,'sin_data'],x_data.loc[:,'cos_data'],c='y',edgecolors='k',s=50,cmap=cm_dark)#样本
plt.scatter(x_test.loc[:,'sin_data'],x_test.loc[:,'cos_data'],s=120,facecolors='none',zorder=10) #quanzhong测试样本
plt.xlabel(u'sin_data',fontsize=13)
plt.ylabel(u'cos_data',fontsize=13)
plt.xlim(x1_min,x1_max)
plt.ylim(x2_min,x2_max)
plt.title(u'支持向量机测试',fontsize=15)
plt.show
