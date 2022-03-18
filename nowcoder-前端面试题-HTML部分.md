# nowcoder-前端面试题-HTML部分

## 浏览器页面有哪三层构成，分别是什么，作用是什么?
- 构成：结构层、表示层、行为层
- 分别是：HTML、CSS、JavaScript
- 作用：HTML实现页面结构，CSS完成页面的表现与风格，JavaScript实现一些客户端的功能与业务。
[Discussion](https://www.nowcoder.com/questionTerminal/09ad0bbbee75416189e665df9095507f)
## HTML5的优点与缺点？
- 优点：a、网络标准统一、HTML5本身是由W3C推荐出来的。
- b、多设备、跨平台
- c、即时更新。
- d、提高可用性和改进用户的友好体验；
- e、有几个新的标签，这将有助于开发人员定义重要的内容；
- f、可以给站点带来更多的多媒体元素(视频和音频)；
- g、可以很好的替代Flash和Silverlight；
- h、涉及到网站的抓取和索引的时候，对于SEO很友好；
- i、被大量应用于移动应用程序和游戏。
- 缺点：a、安全：像之前Firefox4的websocket和透明代理的实现存在严重的安全问题，同时webstorage、websocket这样的功能很容易被黑客利用，来盗取用户的信息和资料。
- b、完善性：许多特性各浏览器的支持程度也不一样。
- c、技术门槛：HTML5简化开发者工作的同时代表了有许多新的属性和API需要开发者学习，像webworker、websocket、webstorage等新特性，后台甚至浏览器原理的知识，机遇的同时也是巨大的挑战
- d、性能：某些平台上的引擎问题导致HTML5性能低下。
- e、浏览器兼容性：最大缺点，IE9以下浏览器几乎全军覆没。
[Discussion](https://www.nowcoder.com/questionTerminal/590a510de9bd49d491e6afd8088403d8)
## Doctype作用? 严格模式与混杂模式如何区分？它们有何意义?
- 回答1：（1）、声明位于文档中的最前面，处于标签之前。告知浏览器的解析器，用什么文档类型规范来解析这个文档。
- （2）、严格模式的排版和JS运作模式是以该浏览器支持的最高标准运行。
- （3）、在混杂模式中，页面以宽松的向后兼容的方式显示。模拟老式浏览器的行为以防止站点无法工作。（4）、DOCTYPE不存在或格式不正确会导致文档以混杂模式呈现。
- 回答2：doctype声明指出阅读程序应该用什么规则集来解释文档中的标记。在Web文档的情况下，“阅读程序”通常是浏览器或者校验器这样的一个程序，“规则”则是W3C所发布的一个文档类型定义（DTD）中包含的规则。
- (1)声明位于文档中的最前面的位置，处于标签之前。此标签可告知浏览器文档使用哪种HTML或XHTML规范。该标签可声明三种DTD类型，分别表示严格版本、过渡版本以及基于框架的HTML文档。
- (2)所谓的标准模式是指，浏览器按W3C标准解析执行代码；怪异模式则是使用浏览器自己的方式解析执行代码，因为不同浏览器解析执行的方式不一样，所以我们称之为怪异模式。严格模式是浏览器根据web标准去解析页面，是一种要求严格的DTD，不允许使用任何表现层的语法，如
- 。严格模式的排版和JS运作模式是以该浏览器支持的最高标准运行混杂模式则是一种向后兼容的解析方法，说的透明点就是可以实现IE5.5以下版本浏览器的渲染模式。
- (3)浏览器解析时到底使用标准模式还是怪异模式，与你网页中的DTD声明直接相关，DTD声明定义了标准文档的类型（标准模式解析）文档类型，会使浏览器使用相应的方式加载网页并显示，忽略DTD声明,将使网页进入怪异模式。
[Discussion](https://www.nowcoder.com/questionTerminal/b982fd49d6ce4ff39b10dd6b5476199b)
## HTML5有哪些新特性、移除了哪些元素？
- Html5新增了27个元素，废弃了16个元素，根据现有的标准规范，把HTML5的元素按优先级定义为结构性属性、级块性元素、行内语义性元素和交互性元素4大类。
- 结构性元素主要负责web上下文结构的定义
- section：在web页面应用中，该元素也可以用于区域的章节描述。
- header：页面主体上的头部，header元素往往在一对body元素中。
- footer：页面的底部（页脚），通常会标出网站的相关信息。
- nav：专门用于菜单导航、链接导航的元素，是navigator的缩写。
- article：用于表现一篇文章的主体内容，一般为文字集中显示的区域。
- 级块性元素主要完成web页面区域的划分，确保内容的有效分割。
- aside：用于表达注记、贴士、侧栏、摘要、插入的引用等作为补充主体的内容。
- figure：是对多个元素进行组合并展示的元素，通常与figcaption联合使用。
- code：表示一段代码块。
- dialog：用于表达人与人之间的对话，该元素包含dt和dd这两个组合元素，dt用于表示说话者，而dd用来表示说话内容。
- 行内语义性元素主要完成web页面具体内容的引用和描述，是丰富内容展示的基础。
- meter：表示特定范围内的数值，可用于工资、数量、百分比等。
- time：表示时间值。
- progress：用来表示进度条，可通过对其max、min、step等属性进行控制，完成对进度的表示和监视。
- video：视频元素，用于支持和实现视频文件的直接播放，支持缓冲预载和多种视频媒体格式。
- audio：音频元素，用于支持和实现音频文件的直接播放，支持缓冲预载和多种音频媒体格式。
- 交互性元素主要用于功能性的内容表达，会有一定的内容和数据的关联，是各种事件的基础。
- details：用来表示一段具体的内容，但是内容默认可能不显示，通过某种手段（如单击）与legend交互才会显示出来。
- datagrid：用来控制客户端数据与显示，可以由动态脚本及时更新。
- menu：主要用于交互菜单（曾被废弃又被重新启用的元素）。
- command：用来处理命令按钮。
[Discussion](https://www.nowcoder.com/questionTerminal/a99c642a9fd94424a68b03c7675a05b8)
## 你做的网页在哪些浏览器测试过,这些浏览器的内核分别是什么?
- a、IE:trident内核
- b、Firefox：gecko内核
- c、Safari:webkit内核
- d、Opera:以前是presto内核，Opera现已改用GoogleChrome的Blink内核
- e、Chrome:Blink(基于webkit，Google与OperaSoftware共同开发)
[Discussion](https://www.nowcoder.com/questionTerminal/b0885d300d0f4229bb3f28e91bfcc065)
## 每个HTML文件里开头都有个很重要的东西，Doctype，知道这是干什么的吗？
- 声明位于文档中的最前面的位置，处于标签之前。此标签可告知浏览器文档使用哪种HTML或XHTML规范。（重点：告诉浏览器按照何种规范解析页面）
[Discussion](https://www.nowcoder.com/questionTerminal/d35ebf720e89492bac565582878ad356)
## 说说你对HTML5认识?（是什么,为什么）
- 是什么：
- HTML5指的是包括HTML、CSS和JavaScript在内的一套技术组合。它希望能够减少网页浏览器对于需要插件的丰富性网络应用服务（Plug-in-BasedRichInternetApplication，RIA），例如：AdobeFlash、MicrosoftSilverlight与OracleJavaFX的需求，并且提供更多能有效加强网络应用的标准集。HTML5是HTML最新版本，2014年10月由万维网联盟（W3C）完成标准制定。目标是替换1999年所制定的HTML4.01和XHTML1.0标准，以期能在互联网应用迅速发展的时候，使网络标准达到匹配当代的网络需求。
- 为什么：
- HTML4陈旧不能满足日益发展的互联网需要，特别是移动互联网。为了增强浏览器功能Flash被广泛使用，但安全与稳定堪忧，不适合在移动端使用（耗电、触摸、不开放）。
- HTML5增强了浏览器的原生功能，符合HTML5规范的浏览器功能将更加强大，减少了Web应用对插件的依赖，让用户体验更好，让开发更加方便，另外W3C从推出HTML4.0到5.0之间共经历了17年，HTML的变化很小，这并不符合一个好产品的演进规则。
[Discussion](https://www.nowcoder.com/questionTerminal/b05a61f9e66b4ccaa15d092131c78e4c)
## 对WEB标准以及W3C的理解与认识?
- 标签闭合、标签小写、不乱嵌套、提高搜索机器人搜索几率、使用外链css和js脚本、结构行为表现的分离、文件下载与页面速度更快、内容能被更多的用户所访问、内容能被更广泛的设备所访问、更少的代码和组件，容易维护、改版方便，不需要变动页面内容、提供打印版本而不需要复制内容、提高网站易用性。
[Discussion](https://www.nowcoder.com/questionTerminal/1a9aea79311f4789bfd381acfe8810b2)
## HTML5行内元素有哪些,块级元素有哪些, 空元素有哪些?
- (1)行内元素
- a-锚点
- *abbr-缩写
- *acronym-首字
- *b-粗体(不推荐)
- *bdo-bidioverride
- *big-大字体
- *br-换行
- *cite-引用
- *code-计算机代码(在引用源码的时候需要)
- *dfn-定义字段
- *em-强调
- *font-字体设定(不推荐)
- *i-斜体
- *img-图片
- *input-输入框
- *kbd-定义键盘文本
- *label-表格标签
- *q-短引用
- *s-中划线(不推荐)
- *samp-定义范例计算机代码
- *select-项目选择
- *small-小字体文本
- *span-常用内联容器，定义文本内区块
- *strike-中划线
- *strong-粗体强调
- *sub-下标
- *sup-上标
- *textarea-多行文本输入框
- *tt-电传文本
- *u-下划线
- *var-定义变量
- (2)块元素(blockelement)
- *address-地址
- *blockquote-块引用
- *center-居中对齐块
- *dir-目录列表
- *div-常用块级容易，也是csslayout的主要标签
- *dl-定义列表
- *fieldset-form控制组
- *form-交互表单
- *h1-大标题
- *h2-副标题
- *h3-3级标题
- *h4-4级标题
- *h5-5级标题
- *h6-6级标题
- *hr-水平分隔线
- *isindex-inputprompt
- *menu-菜单列表
- *noframes-frames可选内容，（对于不支持frame的浏览器显示此区块内容
- *noscript-）可选脚本内容（对于不支持script的浏览器显示此内容）
- *ol-排序表单
- *p-段落
- *pre-格式化文本
- *table-表格
- *ul-非排序列表
- 可变元素
- 可变元素为根据上下文语境决定该元素为块元素或者内联元素。
- *applet-javaapplet
- *button-按钮
- *del-删除文本
- *iframe-inlineframe
- *ins-插入的文本
- *map-图片区块(map)
- *object-object对象
- *script-客户端脚本
- (3)空元素(在HTML[1]元素中，没有内容的HTML元素被称为空元素)
- \<br/>//换行
- \<hr>//分隔线
- \<input>//文本框等
- \<img>//图片
- \<link>\<meta>
[Discussion](https://www.nowcoder.com/questionTerminal/82be034e331a47c9893b2ceef5b8b8b3)
## 什么是WebGL,它有什么优点?
- WebGL（全写WebGraphicsLibrary）是一种3D绘图标准，这种绘图技术标准允许把JavaScript和OpenGLES2.0结合在一起，通过增加OpenGLES2.0的一个JavaScript绑定，WebGL可以为HTML5Canvas提供硬件3D加速渲染，这样Web开发人员就可以借助系统显卡来在浏览器里更流畅地展示3D场景和模型了，还能创建复杂的导航和数据视觉化。显然，WebGL技术标准免去了开发网页专用渲染插件的麻烦，可被用于创建具有复杂3D结构的网站页面，甚至可以用来设计3D网页游戏等等。
- WebGL完美地解决了现有的Web交互式三维动画的两个问题：
- 第一，它通过HTML脚本本身实现Web交互式三维动画的制作，无需任何浏览器插件支持;
- 第二，它利用底层的图形硬件加速功能进行的图形渲染，是通过统一的、标准的、跨平台的OpenGL接口实现的。
- 通俗说WebGL中canvas绘图中的3D版本。因为原生的WebGL很复杂，我们经常会使用一些三方的库，如three.js等，这些库多数用于HTML5游戏开发。
[Discussion](https://www.nowcoder.com/questionTerminal/b981e41cb07549f0bc8ef75c5a8d4690)
## 请你描述一下 cookies，sessionStorage 和 localStorage 的区别?
- sessionStorage和localStorage是HTML5WebStorageAPI提供的，可以方便的在web请求之间保存数据。有了本地数据，就可以避免数据在浏览器和服务器间不必要地来回传递。
- sessionStorage、localStorage、cookie都是在浏览器端存储的数据，其中sessionStorage的概念很特别，引入了一个“浏览器窗口”的概念。sessionStorage是在同源的同窗口（或tab）中，始终存在的数据。也就是说只要这个浏览器窗口没有关闭，即使刷新页面或进入同源另一页面，数据仍然存在。关闭窗口后，sessionStorage即被销毁。同时“独立”打开的不同窗口，即使是同一页面，sessionStorage对象也是不同的
- cookies会发送到服务器端。其余两个不会。
- Microsoft指出InternetExplorer8增加cookie限制为每个域名50个，但IE7似乎也允许每个域名50个cookie。Firefox每个域名cookie限制为50个。Opera每个域名cookie限制为30个。Firefox和Safari允许cookie多达4097个字节，包括名（name）、值（value）和等号。Opera许cookie多达4096个字节，包括：名（name）、值（value）和等号。InternetExplorer允许cookie多达4095个字节，包括：名（name）、值（value）和等号。
- 区别：
- -Cookie
- +每个域名存储量比较小（各浏览器不同，大致4K）
- +所有域名的存储量有限制（各浏览器不同，大致4K）
- +有个数限制（各浏览器不同）
- +会随请求发送到服务器
- -LocalStorage
- +永久存储
- +单个域名存储量比较大（推荐5MB，各浏览器不同）
- +总体数量无限制
- -SessionStorage
- +只在Session内有效
- +存储量更大（推荐没有限制，但是实际上各浏览器也不同）
[Discussion](https://www.nowcoder.com/questionTerminal/27c08b3666e84e69874ea6e97e40afdb)
## 说说你对HTML语义化的理解?
- (1)什么是HTML语义化？
- \<基本上都是围绕着几个主要的标签，像标题（H1~H6）、列表（li）、强调（strongem）等等>
- 根据内容的结构化（内容语义化），选择合适的标签（代码语义化）便于开发者阅读和写出更优雅的代码的同时让浏览器的爬虫和机器很好地解析。
- (2)为什么要语义化？
- 为了在没有CSS的情况下，页面也能呈现出很好地内容结构、代码结构:为了裸奔时好看；
- 用户体验：例如title、alt用于解释名词或解释图片信息、label标签的活用；
- 有利于SEO：和搜索引擎建立良好沟通，有助于爬虫抓取更多的有效信息：爬虫依赖于标签来确定上下文和各个关键字的权重；
- 方便其他设备解析（如屏幕阅读器、盲人阅读器、移动设备）以意义的方式来渲染网页；
- 便于团队开发和维护，语义化更具可读性，是下一步网页的重要动向，遵循W3C标准的团队都遵循这个标准，可以减少差异化。
- (3)语义化标签
- \<header>\</header>
- \<footer>\</footer>
- \<nav>\</nav>
- \<section>\</section>
- \<article>\</article>SM:用来在页面中表示一套结构完整且独立的内容部分
- \<aside>\</aside>SM:主题的附属信息(用途很广，主要就是一个附属内容)，如果article里面为一篇文章的话，那么文章的作者以及信息内容就是这篇文章的附属内容了
- \<figure>\</figure>SM:媒体元素，比如一些视频，图片啊等等
- \<datalist>\</datalist>
- SM:选项列表，与input元素配合使用，来定义input可能的值
- \<details>\</details>
- SM:用于描述文档或者文档某个部分的细节~默认属性为open~
- ps:配合summary一起使用
[Discussion](https://www.nowcoder.com/questionTerminal/fe26e5b66a394139a61be8266689c7ea)
## link和@import的区别?
- XML/HTML代码
- \<linkrel='stylesheet'rev='stylesheet'href='CSS文件'type='text/css'media='all'/>
- XML/HTML代码
- \<styletype='text/css'media='screen'>
- @importurl('CSS文件');
- \</style>
- 两者都是外部引用CSS的方式，但是存在一定的区别：
- 区别1：link是XHTML标签，除了加载CSS外，还可以定义RSS等其他事务；@import属于CSS范畴，只能加载CSS。
- 区别2：link引用CSS时，在页面载入时同时加载；@import需要页面网页完全载入以后加载。
- 区别3：link是XHTML标签，无兼容问题；@import是在CSS2.1提出的，低版本的浏览器不支持。
- 区别4：link支持使用Javascript控制DOM去改变样式；而@import不支持。
[Discussion](https://www.nowcoder.com/questionTerminal/ae9f71f950e64c9d82b1b396b7f3bec5)
## 说说你对SVG理解?
- SVG可缩放矢量图形（ScalableVectorGraphics）是基于可扩展标记语言（XML），用于描述二维矢量图形的一种图形格式。SVG是W3C('WorldWideWebConSortium'即'国际互联网标准组织')在2000年8月制定的一种新的二维矢量图形格式，也是规范中的网络矢量图形标准。SVG严格遵从XML语法，并用文本格式的描述性语言来描述图像内容，因此是一种和图像分辨率无关的矢量图形格式。SVG于2003年1月14日成为W3C推荐标准。
- 特点：
- (1)任意放缩
- 用户可以任意缩放图像显示，而不会破坏图像的清晰度、细节等。
- (2)文本独立
- SVG图像中的文字独立于图像，文字保留可编辑和可搜寻的状态。也不会再有字体的限制，用户系统即使没有安装某一字体，也会看到和他们制作时完全相同的画面。
- (3)较小文件
- 总体来讲，SVG文件比那些GIF和JPEG格式的文件要小很多，因而下载也很快。
- (4)超强显示效果
- SVG图像在屏幕上总是边缘清晰，它的清晰度适合任何屏幕分辨率和打印分辨率。
- (5)超级颜色控制
- SVG图像提供一个1600万种颜色的调色板，支持ICC颜色描述文件标准、RGB、线X填充、渐变和蒙版。
- (6)交互X和智能化。SVG面临的主要问题一个是如何和已经占有重要市场份额的矢量图形格式Flash竞争的问题，另一个问题就是SVG的本地运行环境下的厂家支持程度。
- 浏览器支持：
- InternetExplorer9，火狐，谷歌Chrome，Opera和Safari都支持SVG。
- IE8和早期版本都需要一个插件-如AdobeSVG浏览器，这是免费提供的。
[Discussion](https://www.nowcoder.com/questionTerminal/c5982f8b70ba427aab804643e12ab44d)
## HTML全局属性(global attribute)有哪些?
- 参考资料：MDN:htmlglobalattribute或者W3CHTMLglobal-attributesaccesskey:设置快捷键，提供快速访问元素如aaa在windows下的firefox中按alt+shift+a可激活元素class:为元素设置类标识，多个类名用空格分开，CSS和javascript可通过class属性获取元素contenteditable:指定元素内容是否可编辑contextmenu:自定义鼠标右键弹出菜单内容data-*:为元素增加自定义属性dir:设置元素文本方向draggable:设置元素是否可拖拽dropzone:设置元素拖放类型：copy,move,linkhidden:表示一个元素是否与文档。样式上会导致元素不显示，但是不能用这个属性实现样式效果id:元素id，文档内唯一lang:元素内容的的语言spellcheck:是否启动拼写和语法检查style:行内css样式tabindex:设置元素可以获得焦点，通过tab可以导航title:元素相关的建议信息translate:元素和子孙节点内容是否需要本地化
[Discussion](https://www.nowcoder.com/questionTerminal/5505ebcd04df48dd91e32977cb9a9b11)
## 说说超链接target属性的取值和作用？
- target这个属性指定所链接的页面在浏览器窗口中的打开方式。
- 它的参数值主要有：
- a、_blank：在新浏览器窗口中打开链接文件
- b、_parent：将链接的文件载入含有该链接框架的父框架集或父窗口中。如果含有该链接的框架不是嵌套的，则在浏览器全屏窗口中载入链接的文件，就象_self参数一。
- c、_self：在同一框架或窗口中打开所链接的文档。此参数为默认值，通常不用指定。但是我不太理解。
- d、_top：在当前的整个浏览器窗口中打开所链接的文档，因而会删除所有框架。
[Discussion](https://www.nowcoder.com/questionTerminal/e79c30255a4844028998097f4f75c85e)
## `data-`属性的作用是什么？
- `data-`为H5新增的为前端开发者提供自定义的属性，这些属性集可以通过对象的`dataset`属性获取，不支持该属性的浏览器可以通过`getAttribute`方法获取:
- 需要注意的是：`data-`之后的以连字符分割的多个单词组成的属性，获取的时候使用驼峰风格。所有主流浏览器都支持data-*属性。
- 即：当没有合适的属性和元素时，自定义的data属性是能够存储页面或App的私有的自定义数据。
[Discussion](https://www.nowcoder.com/questionTerminal/6b7dbb4ce186400b857a7afd64b72346)
## 介绍一下你对浏览器内核的理解？
- 主要分成两部分：渲染引擎(layoutengineer或RenderingEngine)和JS引擎。渲染引擎：负责取得网页的内容（HTML、XML、图像等等）、整理讯息（例如加入CSS等），以及计算网页的显示方式，然后会输出至显示器或打印机。浏览器的内核的不同对于网页的语法解释会有不同，所以渲染的效果也不相同。所有网页浏览器、电子邮件客户端以及其它需要编辑、显示网络内容的应用程序都需要内核。JS引擎则：解析和执行javascript来实现网页的动态效果。最开始渲染引擎和JS引擎并没有区分的很明确，后来JS引擎越来越独立，内核就倾向于只指渲染引擎。
[Discussion](https://www.nowcoder.com/questionTerminal/595df24f5af2428480ba6ef3c392fc34)
## 常见的浏览器内核有哪些？
- viewsourceprint?
- 1.
- Trident内核：IE,MaxThon,TT,TheWorld,360,搜狗浏览器等。[又称MSHTML]
- 2.
- Gecko内核：Netscape6及以上版本，FF,MozillaSuite/SeaMonkey等
- 3.
- Presto内核：Opera7及以上。[Opera内核原为：Presto，现为：Blink;]
- 4.
- Webkit内核：Safari,Chrome等。[Chrome的：Blink（WebKit的分支）]
[Discussion](https://www.nowcoder.com/questionTerminal/9ed05e37c04e45b2a2d95ebe087c4be5)
## iframe有那些缺点？
- *iframe会阻塞主页面的Onload事件；
- *搜索引擎的检索程序无法解读这种页面，不利于SEO;
- *iframe和主页面共享连接池，而浏览器对相同域的连接有限制，所以会影响页面的并行加载。
- 使用iframe之前需要考虑这两个缺点。如果需要使用iframe，最好是通过javascript
- 动态给iframe添加src属性值，这样可以绕开以上两个问题。
[Discussion](https://www.nowcoder.com/questionTerminal/ec1a7ecc8a0c4150b6df6f9a485bc26f)
## Label的作用是什么，是怎么用的？
- label标签来定义表单控制间的关系,当用户选择该标签时，浏览器会自动将焦点转到和标签相关的表单控件上。
- \<labelfor='Name'>Number:\</label>
- \<inputtype=“text“name='Name'id='Name'/>
[Discussion](https://www.nowcoder.com/questionTerminal/87786e5d47b9417caa2e1dc93b5f7037)
## 如何实现浏览器内多个标签页之间的通信?
- WebSocket、SharedWorker；
- 我们通过监听事件，控制它的值来进行页面信息通信；
- 注意quirks：Safari在无痕模式下设置localstorge值时会抛出QuotaExceededError的异常；
[Discussion](https://www.nowcoder.com/questionTerminal/cffb77bcd4f54671aa22a861cb8b6bcb)
## 如何在页面上实现一个圆形的可点击区域？
- a、map+area或者svg
- b、border-radius
- c、纯js实现需要求一个点在不在圆上简单算法、获取鼠标坐标等等
[Discussion](https://www.nowcoder.com/questionTerminal/fe155273580e46dfa2b15875e94a8b96)
## title与h3的区别、b与strong的区别、i与em的区别？
- title属性没有明确意义只表示是个标题，H1则表示层次明确的标题，对页面信息的抓取也有很大的影响；
- strong是标明重点内容，有语气加强的含义，使用阅读设备阅读网络时：\<strong>会重读，而\<B>是展示强调内容。
- i内容展示为斜体，em表示强调的文本；
- PhysicalStyleElements--自然样式标签
- b,i,u,s,pre
- SemanticStyleElements--语义样式标签
- strong,em,ins,del,code
- 应该准确使用语义样式标签,但不能滥用,如果不能确定时首选使用自然样式标签。
[Discussion](https://www.nowcoder.com/questionTerminal/ec2d3e0107014c4ca9647ad91d0907c5)
## 实现不使用 border 画出1px高的线，在不同浏览器的标准模式与怪异模式下都能保持一致的效果？
- \<divstyle="width:100%;height:1px;background-color:black">\</div>
[Discussion](https://www.nowcoder.com/questionTerminal/d92f26f2b98a4e2f9d150c8c123c1724)
## HTML5标签的作用?(用途)
- a、使Web页面的内容更加有序和规范
- b、使搜索引擎更加容易按照HTML5规则识别出有效的内容
- c、使Web页面更接近于一种数据字段和表
[Discussion](https://www.nowcoder.com/questionTerminal/8198277d51e740b290a1ec08d1e5812c)
## 简述一下src与href的区别？
- src用于替换当前元素，href用于在当前文档和引用资源之间确立联系。
- src是source的缩写，指向外部资源的位置，指向的内容将会嵌入到文档中当前标签所在位置；在请求src资源时会将其指向的资源下载并应用到文档内，例如js脚本，img图片和frame等元素。
- \<scriptsrc='js.js'>\</script>
- 当浏览器解析到该元素时，会暂停其他资源的下载和处理，直到将该资源加载、编译、执行完毕，图片和框架等元素也如此，类似于将所指向资源嵌入当前标签内。这也是为什么将js脚本放在底部而不是头部。
- href是HypertextReference的缩写，指向网络资源所在位置，建立和当前元素（锚点）或当前文档（链接）之间的链接，如果我们在文档中添加
- \<linkhref='common.css'rel='stylesheet'/>
- 那么浏览器会识别该文档为css文件，就会并行下载资源并且不会停止对当前文档的处理。这也是为什么建议使用link方式来加载css，而不是使用@import方式。
[Discussion](https://www.nowcoder.com/questionTerminal/9c8efb898bb244f88f2a5ab1b27b972c)
## 谈谈你对canvas的理解？
- canvas是HTML5中新增一个HTML5标签与操作canvas的javascriptAPI，它可以实现在网页中完成动态的2D与3D图像技术。标记和SVG以及VML之间的一个重要的不同是，有一个基于JavaScript的绘图API，而SVG和VML使用一个XML文档来描述绘图。SVG绘图很容易编辑与生成，但功能明显要弱一些。canvas可以完成动画、游戏、图表、图像处理等原来需要Flash完成的一些功能。
[Discussion](https://www.nowcoder.com/questionTerminal/05745bf27bce4b9a9b19831934a839f9)
## WebSocket与消息推送？
- B/S架构的系统多使用HTTP协议，
- HTTP协议的特点：1无状态协议2用于通过Internet发送请求消息和响应消息3使用端口接收和发送消息，默认为80端口底层通信还是使用Socket完成。
- HTTP协议决定了服务器与客户端之间的连接方式，无法直接实现消息推送（F5已坏）,一些变相的解决办法：
- 双向通信与消息推送
- 轮询：客户端定时向服务器发送Ajax请求，服务器接到请求后马上返回响应信息并关闭连接。优点：后端程序编写比较容易。缺点：请求中有大半是无用，浪费带宽和服务器资源。实例：适于小型应用。
- 长轮询：客户端向服务器发送Ajax请求，服务器接到请求后hold住连接，直到有新消息才返回响应信息并关闭连接，客户端处理完响应信息后再向服务器发送新的请求。优点：在无消息的情况下不会频繁的请求，耗费资小。缺点：服务器hold连接会消耗资源，返回数据顺序无保证，难于管理维护。Comet异步的ashx，实例：WebQQ、Hi网页版、FacebookIM。
- 长连接：在页面里嵌入一个隐蔵iframe，将这个隐蔵iframe的src属性设为对一个长连接的请求或是采用xhr请求，服务器端就能源源不断地往客户端输入数据。优点：消息即时到达，不发无用请求；管理起来也相对便。缺点：服务器维护一个长连接会增加开销。实例：Gmail聊天
- FlashSocket：在页面中内嵌入一个使用了Socket类的Flash程序JavaScript通过调用此Flash程序提供的Socket接口与服务器端的Socket接口进行通信，JavaScript在收到服务器端传送的信息后控制页面的显示。优点：实现真正的即时通信，而不是伪即时。缺点：客户端必须安装Flash插件；非HTTP协议，无法自动穿越防火墙。实例：网络互动游戏。
- Websocket:
- WebSocket是HTML5开始提供的一种浏览器与服务器间进行全双工通讯的网络技术。依靠这种技术可以实现客户端和服务器端的长连接，双向实时通信。
- 特点:
- a、事件驱动
- b、异步
- c、使用ws或者wss协议的客户端socket
- d、能够实现真正意义上的推送功能
- 缺点：少部分浏览器不支持，浏览器支持的程度与方式有区别。
[Discussion](https://www.nowcoder.com/questionTerminal/bd4d40203dd04f048870d5ff76d5d709)
## img的title和alt有什么区别？
- Alt用于图片无法加载时显示Title为该属性提供信息，通常当鼠标滑动到元素上的时候显示
[Discussion](https://www.nowcoder.com/questionTerminal/01fb7926a0c8462eb5567801c8f67ba3)
## 表单的基本组成部分有哪些，表单的主要用途是什么？
- 组成：表单标签、表单域、表单按钮
- a、表单标签：这里面包含了处理表单数据所用CGI程序的URL,以及数据提交到服务器的方法。
- b、表单域：包含了文本框、密码框、隐藏域、多行文本框、复选框、单选框、下拉选择框、和文件上传框等。
- c、表单按钮：包括提交按钮，复位按钮和一般按钮；用于将数据传送到服务器上的CGI脚本或者取消输入，还可以用表单按钮来控制其他定义了处理脚本的处理工作。
- 主要用途：表单在网页中主要负责数据采集的功能，和向服务器传送数据。
[Discussion](https://www.nowcoder.com/questionTerminal/ce5f3f096db94858bbd96a7d9585a48c)
## 表单提交中Get和Post方式的区别？
- (1)、get是从服务器上获取数据，post是向服务器传送数据。
- (2)、get是把参数数据队列加到提交表单的ACTION属性所指的URL中，值和表单内各个字段一一对应，在URL中可以看到。post是通过HTTPpost机制，将表单内各个字段与其内容放置在HTMLHEADER内一起传送到ACTION属性所指的URL地址,用户看不到这个过程。
- (3)、对于get方式，服务器端用Request.QueryString获取变量的值，对于post方式，服务器端用Request.Form获取提交的数据。
- (4)、get传送的数据量较小，不能大于2KB。post传送的数据量较大，一般被默认为不受限制。但理论上，IIS4中最大量为80KB，IIS5中为100KB。
- (5)、get安全性低，post安全性较高。
[Discussion](https://www.nowcoder.com/questionTerminal/a558b2de11a34d2f83910f7d83220290)
## HTML5 有哪些新增的表单元素？
- HTML5新增了很多表单元素让开发者构建更优秀的Web应用程序，主要有：datalistkeygenoutput
[Discussion](https://www.nowcoder.com/questionTerminal/7ffb0dfd4a944c2898c98148dee56c55)
## HTML5 废弃了哪些 HTML4 标签？
- HTML5废弃了一些过时的，不合理的HTML标签：
- ·frame
- ·frameset
- ·noframe
- ·applet
- ·big
- ·center
- ·basefont
[Discussion](https://www.nowcoder.com/questionTerminal/61c01db3031a4d91a3c4df6de1fddd91)
## HTML5 标准提供了哪些新的 API？
- HTML5提供的应用程序API主要有：
- ·MediaAPI
- ·TextTrackAPI
- ·ApplicationCacheAPI
- ·UserInteraction
- ·DataTransferAPI
- ·CommandAPI
- ·ConstraintValidationAPI
- ·HistoryAPI
[Discussion](https://www.nowcoder.com/questionTerminal/021a9a324bb04123abd2094a085a1865)
## HTML5 存储类型有什么区别？
- HTML5能够本地存储数据，在之前都是使用cookies使用的。HTML5提供了下面两种本地存储方案：
- ·localStorage用于持久化的本地存储，数据永远不会过期，关闭浏览器也不会丢失。
- ·sessionStorage同一个会话中的页面才能访问并且当会话结束后数据也随之销毁。因此sessionStorage不是一种持久化的本地存储，仅仅是会话级别的存储
[Discussion](https://www.nowcoder.com/questionTerminal/e0ba391887af4cb78d2d7de958f57eac)
## HTML5 应用程序缓存和浏览器缓存有什么区别？
- 应用程序缓存是HTML5的重要特性之一，提供了离线使用的功能，让应用程序可以获取本地的网站内容，例如HTML、CSS、图片以及JavaScript。这个特性可以提高网站性能，它的实现借助于manifest文件，如下：
- \<!doctypehtml>
- \<htmlmanifest=”example.appcache”>
- …..
- \</html>
- 与传统浏览器缓存相比，它不强制用户访问的网站内容被缓存。
[Discussion](https://www.nowcoder.com/questionTerminal/af6801e0e4c844e8a07590c58a313784)
## HTML5 Canvas 元素有什么用？
- Canvas元素用于在网页上绘制图形，该元素标签强大之处在于可以直接在HTML上进行图形操作，
- \<canvasid=”canvas1″width=”300″height=”100″>
- \</canvas>
[Discussion](https://www.nowcoder.com/questionTerminal/77602347b5ea4a7aa1f5d81064176795)
## 除了 audio 和 video，HTML5 还有哪些媒体标签？
- HTML5对于多媒体提供了强有力的支持，除了audio和video标签外，还支持以下标签：
- \<embed>标签定义嵌入的内容，比如插件。
- \<embedtype=”video/quicktime”src=”Fishing.mov”>
- \<source>对于定义多个数据源很有用。
- \<videowidth=”450″height=”340″controls>
- \<sourcesrc=”jamshed.mp4″type=”video/mp4″>
- \<sourcesrc=”jamshed.ogg”type=”video/ogg”>
- \</video>
- \<track>标签为诸如video元素之类的媒介规定外部文本轨道。用于规定字幕文件或其他包含文本的文件，当媒介播放时，这些文件是可见的。
- \<videowidth=”450″height=”340″controls>
- \<sourcesrc=”jamshed.mp4″type=”video/mp4″>
- \<sourcesrc=”jamshed.ogg”type=”video/ogg”>
- \<trackkind=”subtitles”label=”English”src=”jamshed_en.vtt”srclang=”en”default>\</track>
- \<trackkind=”subtitles”label=”Arabic”src=”jamshed_ar.vtt”srclang=”ar”>\</track>
- \</video>
[Discussion](https://www.nowcoder.com/questionTerminal/ccea2548d5994150a77c1f9c869bf674)
## HTML5 中如何嵌入视频？
- 和音频类似，HTML5支持MP4、WebM和Ogg格式的视频，下面是简单示例：
- \<videowidth=”450″height=”340″controls>
- \<sourcesrc=”jamshed.mp4″type=”video/mp4″>
- Yourbrowserdoes’ntsupportvideoembeddingfeature.
- \</video>
[Discussion](https://www.nowcoder.com/questionTerminal/f45c7428912646369697623c00bb4412)
## HTML5 中如何嵌入音频？
- HTML5支持MP3、Wav和Ogg格式的音频，下面是在网页中嵌入音频的简单示例：
- \<audiocontrols>
- \<sourcesrc=”jamshed.mp3″type=”audio/mpeg”>
- Yourbrowserdoes’ntsupportaudioembeddingfeature.
- \</audio>
[Discussion](https://www.nowcoder.com/questionTerminal/cc8e8d4db9d94d078011c4401dd6ac01)
## 新的 HTML5 文档类型和字符集是？
- HTML5文档类型很简单：
- \<!doctypehtml>
- HTML5使用UTF-8编码示例：
- \<metacharset=”UTF-8″>
[Discussion](https://www.nowcoder.com/questionTerminal/31dfd4d499bf4d0cb3362cbae7abeee8)
