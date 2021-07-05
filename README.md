# Shihu-Cat-Image-Recognition-System

一、	題目與背景動機
1.	題目
&emsp;&emsp;時護(石虎)系統-石虎與虎斑貓影像辨識<br>
2.	背景動機
&emsp;&emsp;生活在淺山地區的石虎(海拔1500公尺以下)也是人類居住、活動、農耕頻繁的區域。除了面對大自然的考驗外，更要直接面對人類所造成的傷害(工程建設、造橋開路與農耕放牧等行為)，人類棄養或放養的犬貓，入侵到淺山生態系裡，也可能對石虎造成競爭、傷害和傳播疾病[1]。由於道路開入淺山地區，使得石虎有機會進入路面並遭到車輛撞擊，石虎路死事件層出不窮。曾經在臺灣廣泛分布的石虎，如今數量可能已少於500隻，若不加以保護恐將消失在臺灣[2]。<br>
&emsp;&emsp;先前公路單位已在高速公路特定路段設置隔離網和生物通道[3]，新創公司也開發出一款辨識石虎的人工智慧模型，協助在石虎靠近道路時進行偵測，警告牠們應該遠離馬路，減少直接穿越馬路的機會[4]，然而道路以外的地方仍然會有石虎出沒，這些地方沒有科技的幫助，儼然成為保育死角。<br>
&emsp;&emsp;以現階段來說守護石虎還是需要靠大眾的力量，在發現受傷、死亡石虎或是撿到石虎小寶寶進行通報並拍照，讓石虎在安全、有效率的救援下，提高獲救的機會[5]。然而石虎的體型和外貌和家貓相當類似，其中又以虎斑貓最為相似，因此常被誤認，甚至有人以為是一般貓咪而想帶回家飼養，因而有觸法之虞[6]，民眾對於石虎的認知以及石虎與貓的分辨能力不足，因此如果能有一個民間使用的石虎影像辨識系統，讓民眾也能輕易快速分辨石虎與貓，提高通報的正確率與效率，將會是一個解決方法。<br>

---

二、	研究目標與預期成果
1.	研究目標
&emsp;&emsp;先前新創公司所開發的石虎影像辨識模型都是在特定場域針對石虎進行影像辨識，可應用的範圍較狹窄，因此本研究除了石虎資料集之外，考量石虎容易誤認為貓、虎斑貓與石虎不易分辨以及不易將虎斑貓以外的品種誤認成石虎，另一原因為台灣虎斑貓數量多，台灣最常見的貓俗稱米克斯(MIX)[7]，米克斯貓是所有混血貓咪的統稱，人們依據貓咪常見的毛色將米克斯貓大致分成七大類：白貓、黑貓、橘貓、賓士貓、三花貓、虎斑貓、玳瑁貓[8]，故加入虎斑貓資料集，進行石虎與虎斑貓影像辨識，同時改善模型辨識石虎的能力並能夠區分石虎與貓的差別。
2.	預期成果
&emsp;&emsp;本研究預期製作出一個石虎與虎斑貓的影像辨識模型，影像資料集當中，由於相關單位及新創公司並未提供石虎影像資料集開放使用，open data上也沒有台灣虎斑貓相關影像資料集，故資料來源使用網路爬蟲抓取google上面相關圖片，並過濾掉與石虎、虎斑貓無關的圖片，透過卷積神經網路（Convolutional Neural Networks，CNN）建立影像辨識模型，此模型可分辨出圖片中的動物為石虎或是虎斑貓。

---

三、	實驗資料與結果
1.	資料來源與處理
&emsp;&emsp;由於相關單位及新創公司並未提供石虎影像資料集開放使用，open data上也沒有台灣虎斑貓相關影像資料集，故資料來源使用Github當中的Scraping-Google-Images-using-Python專案[9]所提供的程式碼，透過網路爬蟲抓取Google上石虎與虎斑貓的圖片，程式運作方式為，在程式裡寫好要抓取的關鍵字、抓取數量並儲存，打開Windows命令提示字元（cmd.exe）執行程式，開始抓取所有圖片的網址，再一次下載所有圖片，為了讓爬蟲程式更容易執行將程式改良為在命令提示字元直接輸入關鍵字和抓取的圖片數量，省去每次從程式當中修改參數的麻煩，並排除開發者程式當中實際圖片數量小於所需圖片數量時，導致陷入無窮迴圈的錯誤。<br>
&emsp;&emsp;資料清理的部分，主要的問題為透過爬蟲下載的圖片，往往是該圖片的目標網站標題含有搜尋的關鍵字，便會出現在搜尋結果，然而圖片中的圖片不見得是石虎或是虎斑貓的照片，故資料清理的部分便去除不相干的圖片，保留真正的石虎與虎斑貓圖片以用於模型訓練，表1為Google圖片爬蟲圖片數量，表2為資料處理後圖片數量。

<center>表1 Google圖片爬蟲圖片數量</center>

|   |石虎|虎斑貓|
:--|:-:|:-:|
應抓取數量|1000張|1000張
實際抓取數量|990張|996張

<center>表2 資料處理後圖片數量</center>

<center>

|   |石虎|虎斑貓|
:--|:-:|:-:|
原有圖片數量|990張|996張
資料處理後圖片數量|339張|631張

</center>

2.	實驗成果
&emsp;&emsp;本研究分為以下四個實驗，實驗一為石虎與虎斑貓全身影像辨識，實驗二使用Haar cascade分類器分割出石虎與虎斑貓的臉部，進行石虎與虎斑貓臉部影像辨識，實驗三為改為自行分割石虎與虎斑貓的臉部，進行石虎與虎斑貓臉部影像辨識，最後實驗四為使用實驗一的全身影像辨識資料集與實驗三自行分割的臉部資料集進行參數調整，觀察準確率的變化。

實驗一：
&emsp;&emsp;石虎與虎斑貓全身影像辨識為透過卷積神經網路（Convolutional Neural Networks，CNN）建立影像辨識模型進行訓練，使用GitHub上影像辨識專案的程式碼[10]，隱藏層為兩層各128個神經元，相關參數設定如下：
1. 訓練、測試資料比例：8:2
2. 輸出層激活函數(output layer activation function)：sigmoid
3. 損失函數(Loss function)：binary_crossentropy
4. 目標圖片大小(Target_size)：64*64
5. 訓練批次大小(Batch_size)：32
6. 訓練週期(Epochs)：15
&emsp;&emsp;使用石虎與虎斑貓全身影像資料集進行模型訓練及預測後，石虎與虎斑貓的辨識率落在80.83%~90.78%之間，圖1為石虎與虎斑貓全身影像辨識準確率。
![圖1 石虎與虎斑貓全身影像辨識準確率.png](https://github.com/KuoYuHong/Shihu-Cat-Image-Recognition-System/blob/main/README%E5%9C%96%E7%89%87/%E5%9C%961%20%E7%9F%B3%E8%99%8E%E8%88%87%E8%99%8E%E6%96%91%E8%B2%93%E5%85%A8%E8%BA%AB%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E6%BA%96%E7%A2%BA%E7%8E%87.png)
<center>圖1 石虎與虎斑貓全身影像辨識準確率</center>

實驗二：
&emsp;&emsp;為了更精進模型準確率，因此增加臉部的辨識模型，額外識別出石虎與虎斑貓的臉，其優點為照片不容易受拍攝時的背景影響，強調出頭部紋路的特徵且一張照片不會有兩隻貓。石虎與虎斑貓臉部偵測技術使用到OpenCV[11]所提供的Haar cascade分類器[12]進行臉部偵測，程式裡導入指定的Haar cascade分類器，並設定兩項參數進行石虎與虎斑貓臉部影像分割：
1. ScaleFactor：濾波器每次搜尋減少的比例
2. minNeighbers：每個目標至少檢測到幾次以上，才可被認定是真數據
&emsp;&emsp;使用Haar cascade分類器分割出的臉部資料集進行模型訓練及預測後，石虎與虎斑貓臉部的辨識率落在88.46%~94.12%之間，分割出石虎與貓臉的資料量太少，模型的準確率較無意義，不足以呈現影像辨識效果，表3為使用Haar cascade分類器前後圖片數量的差異，圖2、圖3、圖4為設定不同參數下石虎與虎斑貓臉部影像辨識準確率。

<center>表3 使用Haar cascade分類器前後圖片數量的差異</center>

<center>

|   |石虎|虎斑貓|
:-:|:-:|:-:|
原有圖片數量|339張|631張
可識別出臉部的圖片數量<br>scaleFactor=1.3, minNeighbors=1|54張|205張
可識別出臉部的圖片數量<br>scaleFactor=1.3, minNeighbors=3|15張|120張
可識別出臉部的圖片數量<br>scaleFactor=1.3, minNeighbors=5|2張|79張

</center>

![圖2 石虎與虎斑貓臉部影像辨識準確率-Haar cascade參數scaleFactor=1.3, minNeighbors=1.png](https://github.com/KuoYuHong/Shihu-Cat-Image-Recognition-System/blob/main/README%E5%9C%96%E7%89%87/%E5%9C%962%20%E7%9F%B3%E8%99%8E%E8%88%87%E8%99%8E%E6%96%91%E8%B2%93%E8%87%89%E9%83%A8%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E6%BA%96%E7%A2%BA%E7%8E%87-Haar%20cascade%E5%8F%83%E6%95%B8scaleFactor%3D1.3%2C%20minNeighbors%3D1.png)
<center>圖2 石虎與虎斑貓臉部影像辨識準確率-Haar cascade參數scaleFactor=1.3, minNeighbors=1</center>
![圖3 石虎與虎斑貓臉部影像辨識準確率-Haar cascade參數scaleFactor=1.3, minNeighbors=3.png](https://github.com/KuoYuHong/Shihu-Cat-Image-Recognition-System/blob/main/README%E5%9C%96%E7%89%87/%E5%9C%963%20%E7%9F%B3%E8%99%8E%E8%88%87%E8%99%8E%E6%96%91%E8%B2%93%E8%87%89%E9%83%A8%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E6%BA%96%E7%A2%BA%E7%8E%87-Haar%20cascade%E5%8F%83%E6%95%B8scaleFactor%3D1.3%2C%20minNeighbors%3D3.png)
<center>圖3 石虎與虎斑貓臉部影像辨識準確率-Haar cascade參數scaleFactor=1.3, minNeighbors=3</center>
![圖4 石虎與虎斑貓臉部影像辨識準確率-Haar cascade參數scaleFactor=1.3, minNeighbors=5.png](https://github.com/KuoYuHong/Shihu-Cat-Image-Recognition-System/blob/main/README%E5%9C%96%E7%89%87/%E5%9C%964%20%E7%9F%B3%E8%99%8E%E8%88%87%E8%99%8E%E6%96%91%E8%B2%93%E8%87%89%E9%83%A8%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E6%BA%96%E7%A2%BA%E7%8E%87-Haar%20cascade%E5%8F%83%E6%95%B8scaleFactor%3D1.3%2C%20minNeighbors%3D5.png)
<center>圖4 石虎與虎斑貓臉部影像辨識準確率-Haar cascade參數scaleFactor=1.3, minNeighbors=5</center>

實驗三：
&emsp;&emsp;由於透過Haar cascade分類器分割出的臉部圖片數量較少，模型難以呈現出臉部辨識情境的效果，因此自行手動分割臉部特徵，來擴充訓練模型使用的資料量，使用自行分割的臉部資料集進行模型訓練及預測後，臉部的辨識率落在86%~92%之間，表4為自行手動分割前後圖片數量的差異，圖5為石虎與虎斑貓臉部影像辨識準確率-自行手動分割圖片。
<center>表4 自行手動分割前後圖片數量的差異</center>

<center>

|   |石虎|虎斑貓|
:-:|:-:|:-:|
原有圖片數量|339張|631張
Haar cascade分類器分割圖片數量|54張|205張
自行手動分割後圖片數量|242張|594張

</center>

![圖5 石虎與虎斑貓臉部影像辨識準確率-自行手動分割圖片.png](https://github.com/KuoYuHong/Shihu-Cat-Image-Recognition-System/blob/main/README%E5%9C%96%E7%89%87/%E5%9C%965%20%E7%9F%B3%E8%99%8E%E8%88%87%E8%99%8E%E6%96%91%E8%B2%93%E8%87%89%E9%83%A8%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98%E6%BA%96%E7%A2%BA%E7%8E%87-%E8%87%AA%E8%A1%8C%E6%89%8B%E5%8B%95%E5%88%86%E5%89%B2%E5%9C%96%E7%89%87.png)
<center>圖5 石虎與虎斑貓臉部影像辨識準確率-自行手動分割圖片</center>

實驗四：
&emsp;&emsp;實驗四當中使用三種不同的方式修改參數，並以該參數進行訓練及預測後與原始參數得出的準確率進行比較：
1. 原始參數
2. 第二層神經元數量改為256個(原為128個)
3. 修改參數訓練批次大小(batchsize)=64(原為32)、每輪訓練週期的步長(steps per epoch)=60(原為40)、驗證批次大小(validation steps)=30(原為20)
4. 結合2與3修改參數的方式
參數改良後全身辨識的最低準確率從80.83%提升至85.41%，臉部辨識的最高準確率從92%提升至93.33%，表5為模型調整參數前後兩種模型準確率比較。
<center>表5 模型調整參數前後兩種模型準確率比較</center>

<center>

|   |全身辨識率|臉部辨識率<br>(自行切割)|
:-:|:-:|:-:|
(1)原始參數|80.83%~90.78%|86%~92%
(2)第二層神經元數量改為256個(原為128個)|75.41%~90.24%|84.67%~93.33%
(3)修改參數batch_size= 64 (原為32)<br>steps_per_epoch= 60 (原為40)<br>validation_steps= 30 (原為20)|82.96%~90.71%|88.67%~92%
結合(2)、(3)修改參數方式|85.41%~88.75%|90%~92%

</center>

---

四、	結論與未來展望
1.	結論
&emsp;&emsp;本研究經由實驗發現，在沒有現成的石虎與虎斑貓資料集的情況下，即使使用Google抓取的圖片作為資料集製作模型，對於石虎與虎斑貓的辨識準確率都超過八成，全身辨識準確率落在80.83%~90.78%，臉部辨識準確率92%，參數改良後全身辨識的最低準確率從80.83%提升至85.41%，臉部辨識的最高準確率從92%提升至93.33%，全身與臉部辨識相比，兩者比較之下發現下列現象：
    1. 透過Haar cascade分類器分割臉部圖片後，從得到的圖片數量差異發現該分類器對於虎斑貓、石虎臉部辨識效果有限
    2. 石虎與虎斑貓在臉部差異上為眼周圍白紋圈、白條紋，從準確率看出此臉部辨識模型更能夠分類兩者(石虎、虎斑貓)的不同
    3. 從全身模型改為使用臉部模型後，準確率略微提升，未來準確率是否還有成長空間？需要更多影像資料加入模型訓練才能得知
2.	未來展望
&emsp;&emsp;未來期望此辨識系統，能從其他來源擴充更多影像資料集改善模型準確率，或許可進一步開發成手機APP應用，讓民眾使用手機掃描就知道眼前的是石虎還是虎斑貓，並且可在民眾回傳影像的同時為資料集擴充更多影像資料，讓模型能越來越準確，除了能讓社會大眾有效分辨石虎與虎斑貓，也為保衛石虎的保育工作盡一份心力。

---

五、	參考資料
[1] 台灣石虎的分布數量與生存威脅(2021年)。https://ahutw.info/status.html
[2] 台灣石虎的生存危機(2021年)。http://leopardcat.net/endangered.html
[3] 阿虎加油：石虎保育大使 - 常見問題(2021年)。https://ahutw.info/qa.html
[4] MELODY TU(2019年9月3日)。【台灣石虎靠 AI 來保護】遠離路殺！這套 AI 系統創下首個阻擋石虎過馬路的紀錄。https://buzzorange.com/techorange/2019/09/03/leopard-cat-ai-conservation/
[5] 阿虎加油：石虎保育大使 - 事件通報(2021年)。https://ahutw.info/report.php
[6] 消失中的台灣石虎：辨別石虎：(2021年)。http://leopardcat.net/identify.html
[7] 認識貓咪-米克斯 MIX(2021年)。https://www.istoshare.com/intro/educationInfoItem/%E8%B2%93/1/
[8] 米克斯獨領風騷！米克斯貓花色、性格總整理(2021年2月27日)。https://www.hotpets.com.tw/mix-cats-introduction/
[9] GitHub - debadridtt/Scraping-Google-Images-using-Python(2021年)。https://github.com/debadridtt/Scraping-Google-Images-using-Python
[10] GitHub-ywchiu/digiplus_ai(2019年7月23日)。https://github.com/ywchiu/digiplus_ai
[11] OpenCV - 維基百科，自由的百科全書(2021年)。https://zh.wikipedia.org/wiki/OpenCV
[12] opencv/data/haarcascades at master · opencv/opencv · GitHub(2020年4月13日)。https://github.com/opencv/opencv/tree/master/data/haarcascades
