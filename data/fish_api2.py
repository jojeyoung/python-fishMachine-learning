import numpy as np
import pandas as pd


def getFishData():
    # 도미
    bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                    31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                    35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]

    bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                    500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                    700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

    # 빙어
    smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3,
                    11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]

    smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7,
                    10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

    fish_length = bream_length + smelt_length
    fish_weight = bream_weight + smelt_weight
    fish_target = [1]*35 + [0]*14

    input_larr = np.array(fish_length)
    input_warr = np.array(fish_weight)
    target_arr = np.array(fish_target)

    # 랜덤
    np.random.seed(42)
    index = np.arange(49)
    np.random.shuffle(index)

    # 훈련 세트
    #train_inputlarr = input_larr[index[:35]]
    #train_inputwarr = input_warr[index[:35]]
    #train_target = target_arr[index[:35]]

    #train = np.column_stack((train_inputlarr, train_inputwarr, train_target))
    # print(train)

    # fish_dataFrame = pd.DataFrame(
    #    train, columns=["train_length", "train_weight", "train_target"])
    # print(fish_dataFrame)

    # 테스트 세트
    test_inputlarr = input_larr[index[35:]]
    test_inputwarr = input_warr[index[35:]]
    test_target = target_arr[index[35:]]

    test = np.column_stack((test_inputlarr, test_inputwarr, test_target))
    print(test)

    fish_dataFrame = pd.DataFrame(
        test, columns=["test_length", "test_weight", "test_target"])
    print(fish_dataFrame)

    return fish_dataFrame
