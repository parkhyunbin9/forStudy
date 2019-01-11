import pandas as pd 
from sklearn import svm, metrics

# XOR 연산 
xor_input = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류 
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:,0:1] # data
xor_label = xor_df.ix[:,2] # label

# 데이터 학습 & 예측 
clf = svm.SVC() # svm 객체 생성 
clf.fit(xor_data,xor_label)
pre = clf.predict(xor_data)

# 정답률 구하기
ac_score = metrics.accuracy_score(xor_label,pre)
print(" 정답률 : ", ac_score)