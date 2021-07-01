import os
from shutil import copyfile
from sklearn.model_selection import train_test_split

def copyFileToDst(dataset, datafolder, srcfolder):
    for f in dataset:
        src = srcfolder+ f
        dst = datafolder+srcfolder+f
        copyfile(src, dst)

if __name__ == '__main__':
    
    #需要建立資料夾時執行：
    # os.mkdir('body_dataset')
    # os.mkdir('body_dataset/trainset')
    # os.mkdir('body_dataset/trainset/catbody')
    # os.mkdir('body_dataset/trainset/shihubody')
    # os.mkdir('body_dataset/testset')
    # os.mkdir('body_dataset/testset/catbody')
    # os.mkdir('body_dataset/testset/shihubody')

    #撈出所有儲存的圖片
    cat = os.listdir('catbody/')
    shihu = os.listdir('shihubody/')
    
    #切分訓練測試資料
    cat_train ,cat_test  = \
        train_test_split(cat, test_size = 0.2, random_state = 42)
    shihu_train ,shihu_test  = \
        train_test_split(shihu, test_size = 0.2, random_state = 42)
    print("cat_train:",len(cat_train))
    print("cat_test:",len(cat_test))
    print("shihu_train:",len(shihu_train))
    print("shihu_test:",len(shihu_test))
    #複製到目的地資料夾
    os.mkdir('body_dataset')
    os.mkdir('body_dataset/trainset')
    os.mkdir('body_dataset/trainset/catbody/')
    os.mkdir('body_dataset/trainset/shihubody/')
    os.mkdir('body_dataset/testset')
    os.mkdir('body_dataset/testset/catbody/')
    os.mkdir('body_dataset/testset/shihubody/')
    copyFileToDst(cat_train, 'body_dataset/trainset/', 'catbody/')
    copyFileToDst(shihu_train, 'body_dataset/trainset/', 'shihubody/')
    copyFileToDst(cat_test, 'body_dataset/testset/', 'catbody/')
    copyFileToDst(shihu_test, 'body_dataset/testset/', 'shihubody/')
    print("ok")