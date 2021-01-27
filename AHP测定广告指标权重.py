import numpy as np
RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}

#采取简化计算
#一致矩阵的任一列向量都是特征向量，一致性尚好的正反互阵的列向量都应近似特征向量，可取平均，选用和法，----取列向量的算数平均
def  get_w(array):
    row=array.shape[0]
    a_axis_0_sum=array.sum(axis=0)
    b=array/a_axis_0_sum
    b_axis_1_sum=b.sum(axis=1)  #每一行的特征向量
    w=b_axis_1_sum/row           #归一化特征向量
    AW=(array*w).sum(axis=1)
    max_max=sum(AW/(row*w))    #对位相除  lambda
    CI=(max_max-row)/(row-1)
    CR=CI/RI_dict[row]
    if CR<0.1:
        return w
    else:
        print(round(CR,3))
        print('不满足一致性，请进行修改')

def  main(array):
    if type(array) is np.ndarray:
        return get_w(array)
    else:
        print('请输入numpy对象')

if __name__=='__main__':
    e=np.array([[1,1/3,3],[3,1,5],[1/3,1/5,1]])
    e=main(e)
    print(e)
    #对广告数据进行一致测定
    import pandas  as pd
    data=pd.read_excel(r'C:\Users\ant.zheng\Desktop\dataset\PCA\Lazada-ID.xls',sheet_name='ads')
    s=data['SPEND']/data['SPEND'].sum() #依照总和进行归一化
    ct=data['CTR']/data['CTR'].sum()
    cv=data['CVR']/data['CVR'].sum()
    try:
        res=np.array([s,ct,cv])
        ret=(np.transpose(res)*e).sum(axis=1)
        print(ret)
    except TypeError:
        print('数据不满足一致性,可能需要修改')



