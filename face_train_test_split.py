import os
from shutil import copyfile
from sklearn.model_selection import train_test_split

def copyFileToDst(dataset, datafolder, srcfolder):
    for f in dataset:
        src = srcfolder+ f
        dst = datafolder+srcfolder+f
        copyfile(src, dst)

if __name__ == '__main__':
    
    _v = '1.3-5' #version
    # _v = '' #version
    _ = 'face_dataset'+_v #face_dataset
    #需要建立資料夾時執行：
    os.mkdir(_)
    os.mkdir(_+'/trainset')
    os.mkdir(_+'/trainset/catface'+_v+'/')
    os.mkdir(_+'/trainset/shihuface'+_v+'/')
    os.mkdir(_+'/testset')
    os.mkdir(_+'/testset/catface'+_v+'/')
    os.mkdir(_+'/testset/shihuface'+_v+'/')
    
    #撈出所有儲存的圖片
    cat = os.listdir('catface'+_v+'/')
    shihu = os.listdir('shihuface'+_v+'/')
    
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
    copyFileToDst(cat_train, _+'/trainset/', 'catface'+_v+'/')
    copyFileToDst(shihu_train, _+'/trainset/', 'shihuface'+_v+'/')
    copyFileToDst(cat_test, _+'/testset/', 'catface'+_v+'/')
    copyFileToDst(shihu_test, _+'/testset/', 'shihuface'+_v+'/')
    print("ok")