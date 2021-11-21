# OCR是什么？

光学字符识别（Optical Character Recognition, OCR）是指对文本资料的图像文件进行分析识别处理，获取文字及版面信息的过程。亦即将图像中的文字进行识别，并以文本的形式返回。

# 目前发展现状

ocr的发展已经有了非常多的积累，一般人或者企业使用， 都是直接使用第三方的服务，目前提供第三方服务的大企业也非常多，百度，阿里云，腾讯等等，都提供了非常方便的api接口，可以进行调用，识别的速度、精确度和效果也都是非常不错的。唯一的缺点就是api的调用是需要收费的，对于调用频次不高的个人和企业，这个费用还是非常低的。


## 为什么企业要使用开源的而不是直接使用api服务？

目前因为公司的现状，使用开源的有几个目的

1. 每天调用的频次比较高 ， 以后可能越来越高， 所以基于费用的考虑是最主要的。
2. 目前ocr的算法研究基本趋于成熟，并且目前对识别的精度要求不是太高，目前开源项目基本能够满足
3. 对于cv和深度学习进行一定程度的积累和了解，为后续工作做一些铺垫
4. 学习开源ocr的模型构建，方便后续对于模型的更新


## 目前开源的项目现状

目前针对ocr的相关开源项目也还是有不少的，作者正好是公司也需要类似的功能，所以做了一些简单的调研，在这里进行记录。

对于调研不准确的希望大家指出

1.  [Tesseract](https://github.com/tesseract-ocr/tesseract) 
2.  [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 
3.  [EasyOCR](https://github.com/JaidedAI/EasyOCR) 
4.  [chineseocr](https://github.com/chineseocr/chineseocr)
5.  [chineseocr_lite](https://github.com/DayBreak-u/chineseocr_lite)
6.  [TrWebOCR](https://github.com/alisen39/TrWebOCR)
7.  [cnocr](https://github.com/breezedeus/cnocr)



### tesseract
[Tesseract](https://github.com/tesseract-ocr/tesseract) 是谷歌开发并开源的图像文字识别引擎，使用python开发。

#### 优势
1. github上面star非常多，项目非常活跃
2. 识别的语言和文字非常多
3. 后面做背书的公司非常强（google）

#### 劣势
1. 不是专门针对中文场景
2. 相关文档主要是英文，对于阅读和理解起来有一定困难
3. 学习成本比较高
4. 源码较多，并且部分源码是c++，学习起来难度比较大

所以针对目前公司的现状，放弃了这个项目的学习和调研

### PaddleOCR
[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 是百度开源的中文识别的ocr开源软件

#### 优势
1. github上面star非常多，项目非常活跃
2. 模型只针对中文进行训练
3. 后面做背书的公司非常强（baidu）
4. 相关的中文文档非常齐全
5. 识别的精确度比较高

#### 劣势
1. 目前使用的训练模型是基于百度公司自己的PaddlePaddle框架，对于小公司来说并不主流（对比于ts或者pytorch），所使用深度学习框架为后续其他深度学习无法做很好的铺垫
2. 项目整体比较复杂，学习成本较高


### EasyOCR
[EasyOCR](https://github.com/JaidedAI/EasyOCR) 是一个用 Python 编写的 OCR 库，用于识别图像中的文字并输出为文本，支持 80 多种语言。

#### 优势
1. github上面的star也是比较多，但是最近不是特别活跃
2. 支持的语言也是非常多的，多达80多种
3. 识别的精确度尚可

#### 劣势
1. 从官方的页面体验来说识别的速度较慢
2. 识别的文字种类多，学习难度较高
3. 相关的官方文档是基于英文的，学习难度较高，对于新手不太友好

### chineseocr
[chineseocr](https://github.com/chineseocr/chineseocr)

#### 优势
1. github上面的star也是比较多
2. 专门针对中文进行学习和训练的模型
3. 相关的文档比较多，上手相对比较容易

#### 劣势
1. 因为没有大厂和公司的背书， 所以存在一些bug
2. 对于复杂场景下的效果不佳
3. 模型都是现成的，如果要新训练模型难度比较高

### chineseocr_lite
[chineseocr_lite](https://github.com/DayBreak-u/chineseocr_lite)

#### 优势
1. github上面的star也是比较多
2. 专门针对中文进行学习和训练的模型
3. 相关的文档比较多，上手相对比较容易
4. 比较轻量级，部署也比较方便

### TrWebOCR
[TrWebOCR](https://github.com/alisen39/TrWebOCR)

#### 优势
1. 部署简单
2. 使用简单
3. 有对应的web页面，测试方便
4. 有对应的web接口，方便调用


#### 劣势
1. 核心模型不开源，无法进行再次学习
2. 无法进行后续训练
3. 必须要联网才能使用
4. 精度识别一般
5. 项目不是很活跃

### cnocr
[cnocr](https://github.com/breezedeus/cnocr)

#### 优势
1. 使用简单
2. 文档齐全
3. 代码全部开源，可以进行修改
4. 预定义的模型较多
5. 便于学习和模型重新训练

#### 劣势
1. 精确度不高
2. 没有对应的web界面和接口
3. 需要配合cnstd进行使用

## 结论

针对上面的比较讨论，同时根据现在的公司的情况和之前既定的一些目标，暂时选择最简单的cnocr进行学习和内部学习和使用。同时也针对目前cnocr仅仅是一个python包，而且无法通过接口进行调用的情况，做了一个补充项目[hn_ocr](https://github.com/cnhnkj/hn_ocr)。

目前放到github上面，欢迎大家一起学习和完善。






