# 1번

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


import random

# SeedNum for Reproducible
seed_num = 3
np.random.seed(seed_num)
random.seed(seed_num)
tf.random.set_seed(seed_num)

session_conf = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=1,
                                        inter_op_parallelism_threads=1)
sess = tf.compat.v1.Session(graph=tf.compat.v1.get_default_graph(),
                            config=session_conf)

tf.compat.v1.keras.backend.set_session(sess)

session_conf = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=1,
                                        inter_op_parallelism_threads=1)
sess = tf.compat.v1.Session(graph=tf.compat.v1.get_default_graph(),
                            config=session_conf)

tf.compat.v1.keras.backend.set_session(sess)

# 4번 (적절한 전처리...?)
# 데이터 랜덤 셔플
# why? (값이 정렬이 되어있을 수 있기 때문)
# 이후에 실 데이터 활용시 결축치 검사같은것을 진행하면 된다.

cancer = load_breast_cancer()
x = cancer.data
y = cancer.target

idx = np.arange(x.shape[0])
np.random.shuffle(idx)
x = x[idx]
y = y[idx]

# 2번 (데이터의 20%를 테스트 데이터 세트로 분류)
# 이후 train_all은 훈련, 검증셋으로 다시 분류
x_train_all, x_test, y_train_all, y_test = train_test_split(x, y, stratify=y, test_size=.2)

# 3번 (데이터의 60%를 훈련 세트로, 나머지를 검증세트로 설정)

x_train, x_val, y_train, y_val = train_test_split(x_train_all, y_train_all, stratify=y_train_all, test_size=0.25)

# 5번 (분류 알고리즘 구현)
# 여기서는 keras의 Sequential 모델을 사용
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

# 5번 (분류 알고리즘 구현)
# 옵티마이저 함수를 Adam 으로 설정하고 Learning rate를 0.0001로 설정하였다.
# 손실 함수는 이진 크로스엔트로피 함수를 활용하고
# 정확도 수치는 accuracy key 값에 저장한다.

optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=optimizer,
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 모델에 훈련세트를 입력,
# 검증 데이터 셋을 활용해 검증
# epoch 100회 순회 하고 배치 사이즈 32로 설정

history = model.fit(x_train, y_train,
                    validation_data=(x_val, y_val),
                    epochs=100,
                    batch_size=32)

# 6번 ( 정확도 그래프 출력 )
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# 6번 ( 손실 그래프 출력 )
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend('Train', loc='upper left')
plt.show()

train_res = model.evaluate(x_train, y_train)
test_res = model.evaluate(x_test, y_test)
print('train loss =', train_res[0])
print('train acc = ', train_res[1])
print('test  loss =', test_res[0])
print('test  acc = ', test_res[1])


model.summary()