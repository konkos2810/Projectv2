from keras.layers import Dense,Flatten

def fc(encode):
    flat = Flatten()(encode)
    dense = Dense(128, activation='relu')(flat)
    out = Dense(10, activation='softmax')(dense)
    return out