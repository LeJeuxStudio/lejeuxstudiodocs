# Amzn广告策略

## Menu
*  [Background Knowledge](#background)
*  [Match Type](#type)
*  [Match Scenarios](#scenarios)
*  [Strategy](#strategy)
*  [Lower ACoS](#acos)

## <a name="background"></a>Background Knowledge
Campaign（广告活动）: 每个产品的广告分为两大种
> a. Auto广告 - 亚马逊自动生成
> b. manual广告 - 需要自己选择targeting word - Broad/phrase/exact match

Ad groups（广告组）：每个广告组里包含了我们期待别人找到我们产品的**关键词**。相同产品的广告。每个月需要调整，不然会被亚马逊定义为inactive ad group。可调整的内容包括search report，增加关键词，bid（上下5%）等。一组20个词左右为宜。

![alt text](https://cdn.shortpixel.ai/spai/w_1551+q_lossy+ret_img+to_webp/https://tinuiti.com/wp-content/uploads/legacysitecontent/cpcs/posts_01/2018/12/28144825/sp3.png "n")

A10算法：亚马逊推荐产品的算法。与算法越与之匹配的产品被推荐给用户的几率更高。

ACoS: Advertising Cost of Sale （ad spend / sales）。

Bid:　你愿意为一个广告所支付的最高价格

Click through Rate: Clicks / Impression. E.g. 产品被投放到100个用户面前但只有一个人点击了。得到 1/100 = 1%。平均低于1%。

Clicks: 当用户真的点击进入了产品

Cost per Clicks: 每点击一次的价格

Long Tail Keyword (长尾关键词)：比较长，往往是2-3个词组成，甚至是短语，存在于内容页面，除了内容页的标题，还存在于内容中。搜索量非常少，并且不稳定。长尾关键词带来的客户，转化为网站产品客户的概率比目标关键词高很多，因为长尾词的目的性更强. 
![alt text](https://ahrefs.com/blog/wp-content/uploads/2019/09/wl-c.jpg "Logo Title Text 1")


New Product Honeymoon: 新品上架时，亚马逊无法估计新品的转换率。在预估一个转化率的同时会给予较高的曝光度，如果转化率达标，则提升排名，反之亦然。

## <a name="type"></a>Match Type

|Match Type|	Definition|Sample|Would Show|Pros and Cons|
|:---:|:---:|:---:|:---:|:---:|
|Broad Match|Any word in your key phrase|Luxury car| luxury cars, fast cars, luxury apartments, expensive vehicles|可以接触到更多的人群。每次被show都要付钱，所以费钱|
|Phrase Match|keywords in the exact order|Luxury car| luxury car, Good luxury car, Luxury car supplier|接触到更少的人群但是节约了费用，使用时要考虑到用户不一定按你规定的词序搜索（不需要开）|
|Exact Match|Exact match|Luxury car|Luxury car|只能显示给特定的用户看，并不实用，拓展性低|

![alt text](https://pic.cifnews.com/upload/201903/13/201903131449429251.jpg "Logo Title Text 1")

## <a name="scenarios"></a>Match Scenarios
Broad Match 使用场景：提高曝光度阶段（high bid， 低转化率），抓住潜在长尾词客户（0.25 avg bid， 高转化率，该用户会比较少），搜索量小。
Phrase Match 使用场景：用长尾词的情况（low bid， high impression）
Exact Match 使用场景：当且仅当长尾词是个高转换率词的时候
注：不同搜索量的词应该放在不同的ad group给予不同的bid。


## <a name="strategy"></a>Strategy
### Step 1 - 收集关键词 通过反向查找同类产品的关键词
### Step 2 - 设定Campaign
> #### 自动 + Broad（3组） + Exact（10组）[每组20个词]
自动广告
>> 自动广告不是为了盈利。是为了得到新关键词。新关键词可以被放到broad和exact里。
>> 自动广告bid的模式为dynamic up and down，价格可以是suggested bid的125%
>> Negative keywords放准备放在broad和exact里的keywords

> Broad & Exact 
>> budget为自动广告budget的150%
>> exact bid的模式为dynamic up and down，价格可以是suggested bid的125%
>> keywords为sellersprite上得到的

### Step 3 - 复盘
> 每周查看自动广告的report
> 将report里得到的新keywords放到Step 2的Broad & Exact广告组

Note: 每次应用一个strategy的时候耐心等待15天

## <a name="acos"></a>Lower ACOS
https://www.youtube.com/watch?v=xLDQx-gviVE