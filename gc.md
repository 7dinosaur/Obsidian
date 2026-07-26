### 摘要：
更快的旅行速度是人类永恒的追求，研究高超声速条件下声爆波系中激波-膨胀波的合并与衰减机理，并建立相应的声爆抑制方法，是为发展高超声速民机扫清障碍的基础支撑。
<!--指出重要性-->
高超声速条件下声爆的演化与超声速存在显著区别：①强非线性使近场波系很快合并，分散的波系极易演化为N波；②更远的传播距离下非均匀大气效应更显著，声爆信号远场衰减规律更复杂。
<!--高超与超存在显著区别-->
因此，本项目拟开展面向高超声速民机声爆抑制的激波-膨胀波系合并与衰减机理研究，解决两个关键科学问题：①高超声速强非线性作用下近场声爆波系的合并机制；②声爆波系在非均匀大气中远距离传播的衰减机理。研究思路为：首先，发展考虑真实气体效应与熵修正的近/远场声爆数值模拟方法，解决现有方法在高超声速不适用的问题；其次，发展三维数值纹影方法来揭示近场波系的合并机理；然后，研究波系在分层大气和大气边界层中传播的衰减机理；最后，发展针对高超声速民机的声爆抑制方法。项目可拓展现有声爆研究的边界，为探索高超声速民机的低声爆气动布局设计方法提供参考。
<!--研究思路，感觉不是很清楚-->
### 研究现状：
#### 声爆近场传播的演化机理研究现状
> 📌 故事：传统早期理论仅关注远场标准 N 波，认为机身外形优化意义有限，直到Jones等人根据Whitham理论提出声爆最小化理论，近场波形形态逐渐受到重视，调控近场波形也成为低声爆设计的主要思想，随着计算机技术的发展，对近场波形的调控从低精度的Whitham理论向高可信度的CFD发展，基于CFD技术也出现了一些新的近场波形演化机理，在超声速研究相当丰富的情况下学者们将研究边界推向高超声速，通过实验和CFD计算发现在高超声速条件下传统的Whitham理论不再适用，这也意味着基于Whitham理论的声爆最小化理论在高超条件下的实用性应该被重新评估，基于这个情况学者们对高超下的声爆特性开展了一系列的研究，但现有研究结果仍然集中于完全合并的简单N波，目前对高超声爆的研究与70年代对超声速声爆的视角何其相似，然而在几十年超声速的研究经验告诉我们，高超声速的近场波形演化必然是一个重要的研究方向。


（1）**高超声速声爆计算方法研究现状**
当前高超声速声爆计算方法主要分为快速计算方法与CFD数值模拟。一方面早期对高超声速声爆的计算沿用超声速体系的Whitham修正线化理论、波形参数法等，但在M>5的高超声速条件下小扰动假设失效，需要发展针对高超声速声爆的快速计算方法。1975年Tiegerman提出了首个高超声速的阻力声源模型，但模型将全机等效为点爆炸源，无法考虑沿飞行器轴向的升力分布影响，对有升力构型的计算精度有限；Zou等在Tiegerman模型的基础上引入线源修正，将其拓展到了有升力高超声速构型的计算。另一方面尽管高可信度的CFD数值模拟在过去数十年内经过了长足发展，但由于高超声速流动中具有的强非线性，热平衡，真实气体化学反应等因素，常规的CFD求解器在计算高超声速声爆计算代价极大，且难以考虑真实气体效应等高超特性对声爆波系的影响。针对上述问题，Candler 团队等 [15,21,38] 开发 US3D 高精度反应流求解器，Zou 等 [15] 基于该工具系统开展带动力细长体喷流近场数值模拟；国内学者 [19] 则发展耦合黏性与高温非平衡真实气体效应的 PNS 抛物化计算方法，形成 “近场PNS 高精度CFD求解 + sBOOM远场传播” 的声爆计算框架，该框架可完整复现边界层增厚、层流 - 湍流转捩、高温分子解离带来的近场波形畸变规律。尽管已经出现一系列针对高超声速声爆的计算方法，但考虑化学反应的热化学非平衡计算网格规模庞大，且现有研究大多将飞行器外流与发动机喷流分区隔离求解，难以捕捉相互之间的复杂干扰流场，仍然需要研究兼顾高可信度与计算效率的高超声速声爆计算方法。

（2）**波系形态主导下的声爆近场演化机理研究现状**
{N-JSGD-Complex只用一段}

对声爆近场演化的研究主要可以分为三个阶段：第一阶段为上世纪六十年代， Whitham[1][2]、Thomas[3]等人建立了声爆预测的基本框架，且Whitham指出近场波形在传播中会发生合并、畸变等非线性演化效应，但由于早期声爆实验数据均呈现标准N波形态，学界因此普遍认为飞行器外形仅能影响N波幅值[5]，Jones在此基础上给出了使N波峰值最小的理论下限[6]；第二阶段为70年代，McLean[7]与Hayes[8]发现长机身飞行器的激波合并速率较慢，未完全合并的中场波形可传递至地面，近场波形对声爆的影响开始受到重视，并催生了经典的JSGD声爆最小化理论，该理论构造了一种声爆最小化的近场波形，可使地面信号呈现低声爆的斜坡状形态[6][9][10][11]；第三阶段为90年代至今，学界对近场波系的认识不断深化：如Darden探索出了比斜坡波更优的圆顶状波形[14]，Haas等通过MSID方法将强头激波拆分为多道弱激波以延缓合并[15][16]，此外以X-59为代表的新一代超声速民机布局均呈现出明显不同于JSGD理论的复杂低声爆波系，代表第三阶段的复杂近场波形研究已经得到了充分的应用和验证[18]。

在探索低声爆的近场波系形态的过程中，学界提出了一系列的近场波系演化机理，早期Whitham指出超声速近场具有非线性特征，在特征方程中引入非线性修正项$kF(y)r^{1/2}$，当距离$r$较小的时候修正项与线性项同阶因此不可忽略，同时近场由于非线性较强，远场的$r^{-3/4}$衰减率也不适用，从物理上对近远场做出了区分。后续也陆续提出了波瓣平衡波系冻结等近场机理。但在高超声速条件下由于流动显著复杂，超声速条件下的近场演化机理大多不再适用，于是学界开展了一系列针对高超声速声爆近场波系演化的研究，例如高超声速激波-膨胀波系在1-4倍体长区域就会完全合并，边界层厚度的增加以及转捩的发生会显著放大波系的负压区间和拉长波系长度，以及高超声速喷流对近场波系也存在较大影响。尽管在高超声速声爆已有许多研究成果，然而目前研究大多针对简单N波的峰值大小以及波系持续时间，未能对更为复杂的声爆形态以及高超声速下的非线性演化机理做出明确阐释。

CFD技术发展带来的不仅是更好的近场波系形态的探索，还有对速度边界的延拓。尽管上个世纪七十年代已经通过阿波罗15号返回舱获取了一系列的高超声速声爆数据[19]，并且1975年Tiegerman[20]提出了首个高超声速的阻力声源模型，但80年代后由于高超声速飞行器战略地位的下滑，针对有升力高超声速飞行器声爆的研究一度陷入停滞。直到本世纪由于高超声速商用飞行器的行业热潮兴起[21][22]以及计算机技术的发展，针对高超声速飞行器声爆的研究进入快速发展阶段。Yamashita[23]通过全场CFD模拟定量对比了Whitham理论和波形参数法在高超声速下的适用性边界，证明了在超过5马赫的真实大气条件下传统的声爆解析模型均不再适用，产生了较大误差，为此，针对高超条件的声爆研究具备了必要性。为此，king等[24]发展了考虑真实气体和黏性效应的高超声爆CFD方法，计算范围可覆盖4-15马赫，并基于该方法分析了速度与高度对高超声爆的影响规律[25]，zou等开展了HTV-2的声爆实验[26]并提出了一种基于牛顿模型和线源假设的高超声爆快速计算方法[27]。尽管目前高超声爆数值计算的研究已经有了一定基础，然而受限于高超声速流场的复杂性，现有的研究主要集中于对简单N波幅值的研究，尚未提出对高超声速近场波系形态的调控方法。
综上，对超声速近场波形的研究已经得到了相对充足的发展，而高超声速的近场波形研究仍然处于简单N波阶段。回顾声爆研究的几十年历程，正是从N波幅值的研究到调控近场波系形态的思想跃迁催生了超声速民机低声爆设计技术的快速发展，有鉴于此，可以合理推测，高超声速近场波系形态的演化机理研究必然能够指导高超声速民机低声爆设计技术的发展。

参考文献：

1. WHITHAM G B. The flow pattern of a supersonic projectile[J]. Communications on Pure and Applied Mathematics, 1952, 5(3):301-348. [https://doi.org/10.1002/cpa.3160050305](https://link.wtturl.cn/?target=https%3A%2F%2Fdoi.org%2F10.1002%2Fcpa.3160050305&scene=im&aid=582478&lang=zh "autolink").<**Whitham理论1：轴对称情况**>
2. WHITHAM G B. On the propagation of weak shock waves[J]. Quarterly Journal of Mechanics and Applied Mathematics, 1956, 9(3):290-318.<**Whitham理论2：非轴对称情况（还是无升力）**>
3. Thomas C L. Extrapolation of sonic boom pressure signatures by the waveform parameter method[R]. Hampton: NASA Langley Research Center, 1972.<**波形参数法**>
4. MAGLIERI D J, BOBBITT P J, PLOTKIN K J, et al. Sonic boom: six decades of research[R]. NASA Langley Research Center, NASA/SP-2014-622, 2014.<**声爆六十年，包含了实验数据的内容吧**>
5. Darden C M. Sonic boom theory: its status in prediction and minimization[J]. Journal of Aircraft, 1977, 14(6): 569-576.<**早期综述，佐证早期只关心N波**>
6. Jones L B. Lower bounds for sonic bangs[J]. Journal of the Royal Aeronautical Society, 1961, 65: 433-436.<**最小N波峰值的F函数形式**>
7. McLean F E. Some Nonasymptotic Effects on Sonic Boom[R]. Hampton: NASA Langley Research Center, 1965.<**McLean中场波形能够保持**>
8. Hayes W D. Brief Review of Basic Theory[A]//Seebass A R. Sonic Boom Research[C]. Washington: NASA, 1967:3-7.<**Hayes中场波形能保持**>
9. Seebass R, George A R. Sonic boom minimization including both front and rear shocks[J]. AIAA Journal, 1971, 9(10): 2091-2093.<**JSGD的S**>
10. George A R, Seebass R. Lower bounds for sonic booms in the midfield[J]. AIAA Journal, 1969, 7(8): 1542-1545.<**JSGD的G**>
11. Darden C M. Sonic boom minimization with nose-bluntness relaxation[R]. Hampton: NASA Langley Research Center, 1979.<**JSGD的D**>
12. Li W, Rallabhandi S. Inverse design of low-boom supersonic concepts using reversed equivalent-area targets[J]. Journal of Aircraft, 2014, 51(1): 29-36.<**LSG方法**>
13. Ding Y L, Han Z H, Qiao J L, et al. Inverse design method for low-boom supersonic transport with lift constraint[J]. AIAA Journal, 2023, 61(7): 2840-2853.<**PNFO方法**>
14. Darden C M. Minimization of sonic boom parameters in the real and isothermal atmosphere[R]. Hampton: NASA Langley Research Center, 1975.<**圆顶状波形（这好像跟CFD也没关系）**>
15. Haas A, Kroo I. A Multi-Shock Inverse Design Method for Low-Boom Supersonic Aircraft[C]//50th AIAA Aerospace Sciences Meeting. Nashville: AIAA, 2010.<**把JSGD的强头激波拆成多道弱激波提出MSID方法**>
16. Wintzer M, Kroo I. Optimization and Adjoint-Based CFD for the Conceptual Design of Low Sonic Boom [C]//50th AIAA Aerospace Sciences Meeting, AIAA 2012-0963.<**采用MSID目标作为伴随设计目标**>
17. RALLABHANDI S K, MAVRIS D N. Sonic boom minimization using inverse design and probabilistic acoustic propagation[J]. Journal of Aircraft, 2006, 43(6): 1815-1828. DOI:10.2514/1.20457.<**人工神经网络获得更有工程价值的波形（虽然是大牛但是这篇看起来好垃圾啊）**>
18. NASA. Low Boom Flight Demonstration Overview[R/OL]. (2019-08)[2026-07-17]. [https://www.nasa.gov/mission_pages/lowboom/overview](https://link.wtturl.cn/?target=https%3A%2F%2Fwww.nasa.gov%2Fmission_pages%2Flowboom%2Foverview&scene=im&aid=582478&lang=zh "autolink").<**X-59文档**>
19. HILTON D A, HENDERSON H R, MCKINNEY R. Sonic-boom ground-pressure measurements from Apollo 15 [R]. Washington: NASA, 1972.<**阿波罗返回舱数据来源，也是后面博士论文的数据支撑**>
20. TIEGERMAN B. Sonic booms of drag dominated hypersonic vehicles[D]. Ithaca: Cornell University, 1975.<**首次提出阻力主导型（无升力）的高超声爆解析模型**>
21. Sippel M，Callsen S，Singh S，等. SpaceLiner: the 2025 pre-definition status report[J/OL]. CEAS Space Journal，2026-05-05. <**高超火箭**>
22. Russo G, Voto C, Savino R. S4 - A demonstrator of HYPLANE, a single stage suborbital spaceplane and a hypersonic business jet[J]. Acta Astronautica, 2021, 183:244-254. <**小型商用高超飞行器方案**>
23. Yamashita<**计算了旋成体在高超声速条件下的声爆特性，均匀大气马赫7和真实大气马赫5以下波形参数法与CFD结果基本吻合，Whitham理论有误差，现有快速方法仅能覆盖到5马赫，高空高超的声爆显著低于中超声速**>
24. KING C B, SKOWRON S, MILLER S A E. Fully parabolized hypersonic sonic boom prediction with real gas and viscous effects[J]. AIAA Journal, 2024, 62(5): 1683-1700.<**考虑真实气体和黏性效应的高超声爆CFD方法，可以支撑高超现有方法不适用的观点，计算范围覆盖4-15马赫**>
25. King, C. B., Shepard, C. T., and Miller, S. A. E., Parametric Study of the Hypersonic Near-Field and Sonic Boom from Waveriders using a Fully-Parabolized Approach, AIAA Paper 2024-2106, AIAA SciTech Forum, Orlando, FL, Jan. 8–12, 2024, doi:10.2514/6.2024-2106.<**继承上一篇的CFD方法，算高超乘波体，速度和高度的影响，其中马赫7时近场过压反增但是地面反而下降，没有解释，SPL频谱具有幂律衰减特性，与马赫数无关（应该超声速也符合这种情况吧）**>
26. Zou S, Carr Z, Portoni P, et al. Computational and experimental investigation of near-field sonic boom of a HTV-2 type hypersonic boost gliding vehicle[C]//AIAA SciTech Forum. Orlando: AIAA, 2024. DOI:10.2514/6.2024-0671.<**风洞试验和CFD验证，HTV-2模型，但是压力轨观测到严重的激波-激波干扰**>
27. Zou S, Johnston Z, Candler G V, et al. Rapid hypersonic sonic boom prediction using line-distributed energy impulse formulations with and without lift[C]//AIAA SciTech Forum. National Harbor: AIAA, 2023. DOI:10.2514/6.2023-0816.<**基于牛顿气动模型和线源假设的高超声爆快速计算方法**>

###没用到的文献
	[2]Simplification of Numerical and Analytical Tools for Sonic Boom Description
<说是有中场的计算，但是查不到这篇>
	[6]Callsen S, Wilken J, Sippel M. Analysis of sonic boom propagation and population disturbance of hypersonic vehicle trajectories: S. Callsen et al[J]. CEAS Space Journal, 2025, 17(5): 797-814.
高超声爆研究，不过主要规避策略是跳出大气层
	[7]Bishop J W, Blom P, Carr C, et al. An infrasound source analysis of the OSIRIS-REx sample return capsule hypersonic re-entry[J]. The Journal of the Acoustical Society of America, 2025, 158(6): 4637-4650.
没找到全文，算的是探测器返回舱的声爆，作为高超N波研究的支撑文献吧
	[8]Graziani S, Jäschke J J, Viola N, et al. Sonic Boom Velocity and Altitude Sensitivity Analysis of a Hypersonic Aircraft Concept[J]. SAE International Journal of Advances and Current Practices in Mobility 306418, 2025, 7(6): 2940-2953.
比较正统的高超声爆研究，研究速度和高度的影响，覆盖了1.2-5马赫（话说这也算高超？），可用于高超N波研究的支撑或者说明5马赫以上现有方法难以适用？
	[9]KING C B, SKOWRON S, MILLER S A E. Fully parabolized hypersonic sonic boom prediction with real gas and viscous effects[J]. AIAA Journal, 2024, 62(5): 1683-1700.
考虑真实气体和黏性效应的高超声爆CFD方法，可以支撑高超现有方法不适用的观点
计算范围覆盖4-15马赫（这才是真高超啊）

### 研究内容
#### 声爆自临近空间向地面传播过程中的衰减机理研究
高超声速声爆产生位置接近临近空间且伴随大马赫数，传播过程中受到真实大气的影响与常规超声速声爆有较大差异：一方面是在超过25km的飞行高度下大气稀薄，气体成分也与低空大气存在较大差异，且20km以上的大气温度随海拔增加而提升，存在显著的正温度梯度，分层大气的影响更为显著；另一方面在高马赫数下对应的激波角通常接近10度甚至更小，极小的激波角意味着声射线几乎平行于飞行路径，大气风带来垂向风速剪切在声射线上的作用距离被拉长，熵梯度对衰减的影响变得不可忽视；此外，高马赫数会显著拉长波系头激波与尾膨胀波的距离，当波系传播到大气边界层头激波与尾膨胀波会受到不同的湍流作用从而导致波形发生严重变形，且由于湍流的随机性大大增加了这一变形的预测难度。
因此，高超声速声爆在远场传播中的衰减规律远比超声速复杂，传统认知中的单调衰减不再成立，特定高度层内甚至可能出现幅值反增，针对这一复杂现象，本项内容拟开展三方面的研究：（1）声爆在分层大气中传播激波-膨胀波衰减规律；（2）大气风效应对高超声速波系衰减的影响规律；（3）近地面大气边界层对高超声速波系衰减的影响规律。

### 研究方案
首先，针对0~40km大范围分层大气构建考虑正温度梯度与稀疏大气分子弛豫的真实大气模型，研究激波-膨胀波系在不同大气层级中的衰减特征；然后，基于研究内容1中构建的考虑熵修正的传播模型，研究不同背景风对高超声爆波系的影响规律；最后，针对大气边界层的湍流特性，研究湍流对波形的主要作用形式与其影响规律，发展一种针对低空湍流的置信度修正准则。
#### 声爆在分层大气中传播激波-膨胀波衰减规律
第一步，针对高空条件建立温度与高度的精准变化关系，定量评估在高空正温度梯度下声射线向下扭曲特性；第二步，针对高空稀薄大气对广义Burgers传播模型进行分子弛豫修正，稠密大气的分子振动能守恒方程形式如下：
$$w_{vs}(\rho,T)=\frac{e^*_{vs}-e_{vs}}{\tau_s(h_r)}(s=O_2,N_2)$$
其中$\tau_s(h_r)$表示完全碰撞假设下的弛豫时间，在稀薄大气条件下需要考虑分子有限自由程带来的额外弛豫延迟，定义克努森数$Kn=\lambda/L$，$\lambda$为分子平均自由程，$L$为当地流动特征长度，给出基础修正形式：
$$\tau_{eff}=\tau_s(1+Kn)$$
有效弛豫时间$\tau_{eff}$在低空环境由于分子平均自由程$\lambda$较小约等于原始值$\tau_s$，在高空随着$Kn$增大弛豫时间被延长。第三步基于上述修正传播模型，研究稀薄气体分子弛豫效应与高空非均匀分层大气对激波-膨胀波系的衰减规律，分析波系中不同频率组分在上述条件下的衰减特性。
#### 大气风效应对高超声速波系衰减的影响规律
在确立静止大气中的传播规律后，需引入三维风场以模拟真实飞行环境。需要明晰的是高空环境下大气风并不显著，因此可沿用超声速声爆采用的大气风模型，主要差异在于传播过程中极小的激波角使其对大气风引起的风速切变和熵梯度变化有较高敏感性。因此本文基于前一章考虑熵修正的声爆传播模型对不同马赫数的声爆传播过程开展对比分析，明确熵梯度不可忽略的临界马赫数，以及不同马赫数下熵梯度对波系衰减的影响规律；而后对比分析不同的波系形态在熵修正前后的波系演变与衰减速率异同，籍由修正前后的差异量进行模态分析，进而研究大气风对高超声速波系衰减的影响规律。
#### 近地面大气边界层对高超声速波系衰减的影响规律
最后阶段聚焦于声爆波系穿过大气湍流边界层时的随机畸变。首先采用修正的冯·卡门能谱分布和随机傅里叶模态方法，随高度改变描述湍流强度的风速脉动标准差、温度脉动标准差和湍流积分尺度，并基于这些参数随机采样构建大气湍流环境；在此基础上，探究大气边界层湍流对高超声速波系衰减的影响规律，通过统计大量模拟样本，对湍流后的波系进行归一化并聚类分析，研究大气边界层湍流对高超声爆的主要作用形式分类；基于此分类分析湍流强度对地面声爆响度的影响规律，进而发展一种针对低空湍流的置信度修正准则，建立湍流参数与声爆预测不确定度之间的映射关系，为低声爆设计提供更为鲁棒的评估方法。