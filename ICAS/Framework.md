## Low Boom Design and Analysis of a Blended-wing-body Configuration for Large-sized Supersonic Transport
**Why should we do**
Developing next-generation supersonic transport (SST) is one of the most critical directions for future civil transport, but most existing SST configuration have relatively small seating capacity, which limits their commercial potential.
**How to do**
Aiming at this issue, this paper proposed a 160-seats large supersonic blended-wing-body transport (SBWB) configuration.
**What do you do**
A parametric method for SBWB is developed, and the JSGD inverse design is implemented based on this method. Subsequently, the effects of winglet length and sweep angle on sonic boom characteristics are investigated.
**what is the result**
Based on the above research, a low boom design for the 160-seats SBWB configuration is performed. The ground boom intensity value is optimized to xx PLdB. In summary, the SBWB can effectively improve passenger capacity, and demonstrates favorable feasibility in sonic boom mitigation.
### Introduction
### Methodology
1. CFD method
2. sonic boom prediction method
### Low Boom Design and Analysis
1. Parametric Method and Baseline Configuration Generation
	传统的圆形机身截面直径由客舱所需的最小高度或宽度决定，因此截面积随每排座椅数的提升呈现平方增长，若要应用于大型SST，则机身体积将大幅增加，从而导致声爆设计难度急剧提升，翼身融合布局由于机身采用非圆截面，可以采用更贴合客舱的截面形状以达到更小的体积分布，在相同的座级下所需付出的体积代价；另一方面翼身组合体布局在机翼前缘与机身交界位置，流场上是无升力前体到有升力的突变点，这个特征反映到近场波形中则是会产生一个小尖峰，通常认为BWB布局具有全升力面特征，其不存在升力从无到有的突变点，可能存在波形上的优势，本文也将对这一点进行讨论。
	在传统布局的低声爆设计中通常采用分体设计，即对机身和机翼分别布置FFD控制框，该方法高度依赖设计人员的经验，且在精细匹配截面积分布的阶段设计得到的构型容易出现小幅扭曲，在传统构型上机身小幅扭曲对气动的影响可以忽略不计，但BWB由于全升力面的特点，曲面的扭曲带来的气动代价难以忽视。基于该现状，本文采用全机CST方法作为参数化方法，保证优化过程中外形的整体连续性和光顺性。
	该方法将全机外形用多个封闭的剖面曲线表示，每个剖面都用同阶的CST参数化，剖面之间采用三阶NURBS方法生成曲面保证曲面二阶连续。其余参数包括剖面的前后缘x坐标以及z方向偏移。基于该方法开展低声爆设计可以统一参数框架，无需根据变形后的外形重新生成FFD框重新参数化。
	本文首先设定客舱空间，图1为客舱的侧视图与截面示意，共40排座椅，每排4座，合160座，座椅之间的间距为0.95m，客舱高度为2m，座椅宽度为0.55m。考虑到超声速民机客舱体积较小，若再于上方设置行李架会进一步压缩空间使乘客感到不适，因此客舱内部不布置行李架，在机身后方收缩段存放行李。首先生成对称面形状，考虑客舱长度为36m，全机长度取客舱长度的两倍即72m，由于曲面沿展向延伸时会有一定的收缩，对称面客舱约束高度为2.1m，
	
2. Aerodynamic Analysis of the Baseline Configuration
3. Low-Boom Design
	1. preliminary low boom design
	2. rear body wave analysis
### Conclusion