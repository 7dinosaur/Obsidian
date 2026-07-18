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

（1）**波系形态主导下的声爆近场演化机理研究现状**
尽管Whitham修正线化理论[1][2]、波形参数法[3]等声爆预测方法在上世纪六十年代便已建立，并且Whitham阐述了近场波形在传播过程中发生的合并、畸变等非线性演化效应（简称波形老化“wave aging”），但早期由于声爆实验的数据多来自已有的喷气式战斗机[4]，地面测量数据全部呈现标准的N型波，因此大多数学者认为飞行器外形仅能改变N波的幅值[5]。基于这种认识，Jones根据Whitham理论给出了使N波幅值最小的F函数形式[6]。
70年代McLean[7]、Hayes[8]发现对于机身较长的飞行器，激波合并速度变慢，未完全合并的中场波形可以直接传递到地面，于是人们开始关注近场波形对传播中合并的影响。在这种思想的引导下，Jones[6]，Seebass[9]，George[10]，Darden[11]等人基于Whitham理论推导出了经典的声爆最小化理论，基于该理论的反设计方法被称为JSGD反设计方法。该理论指出通过改变外形调控近场波系可使地面声爆信号呈现***斜坡状形态***，这种形态的地面信号声爆强度远低于N波，时至今日依然在低声爆概念设计阶段被广泛应用。
之后的几十年里随着计算机技术的发展，使用CFD技术直接计算高可信度的声爆信号成为可能，结合高可信度的CFD声爆分析和现代优化手段，发展了更先进的低声爆设计方法如LSG方法[12]、PNFO方法[13]等，同时对于低声爆的近场波系也有了更深的认识。Darden[14]探索了更低声爆的F函数形式，发现了更利于降低声爆的圆顶状近场波系，进一步突破了JSGD理论下的声爆下限；Haas等[15][16]将JSGD理论中的强头激波拆散成多道弱激波提出了MSID方法，阻止合并的同时也降低了波系总能量；Rallabhandi等[17]通过人工神经网络在固定升阻比下获得了更具备工程实用性的近场波形目标。随着更复杂的近场波系形态被发现，也诞生了诸多更先进的低声爆布局，其中代表性的低声爆布局就是NASA的低声爆试验机[18]，巡航声爆强度低于75PLdB，其近场声爆形态与JSGD理论差异甚大，远场信号也不再以斜坡状信号为目标，而是以多级弱激波的形式逼近圆顶状信号，这也说明了更复杂的近场波系在工程实际中已经证明了其实用价值。
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
高超声速飞行器的声爆传播不同于常规超声速的声爆传播，其主要差距来自于高巡航海拔和高马赫数工况。一方面在超过25km的飞行高度下大气稀薄，气体成分也与低空大气存在较大差异，导致更严重的分子弛豫效应，且20km以上的大气温度随海拔增加而提升，声爆传播的大气环境更为复杂，对不同频率的波系组分会产生与常规超声速不同的选择性衰减；另一方面在高马赫数下对应的激波角通常接近10度甚至更小，极小的激波角意味着声射线几乎平行于飞行路径，非均匀分层大气存在的垂直梯度以及大气风带来垂向风速剪切在激波面上被大幅放大，声爆信号对真实大气中存在的各种扰动表现出更高的敏感性。
因此，本项内容拟开展三方面的研究：（1）声爆在分层大气中传播激波-膨胀波衰减规律；（2）大气风效应对高超声速波系衰减的影响规律；（3）近地面大气边界层对高超声速波系衰减的影响规律。
（先这样吧）
### 研究方案
#### 声爆在分层大气中传播激波-膨胀波衰减规律
能不能提出一个衰减因子
压力反增现象要提
高超声速飞行器
分层大气中声爆的衰减机制源于非均匀介质对波系结构的持续调制。本研究拟从“几何扩散-介质吸收-波形演化”三者的耦合效应出发，构建适用于平流层正温度梯度条件的广义衰减模型。核心思路是：将射线管截面积的变化（几何扩散因子J）、大气分层引起的局部声速与密度梯度、以及分子弛豫吸收三项纳入统一的衰减因子表达式 αeff(z)αeff​(z)，该因子将不再是常数，而是传播高度和路径长度的函数。

关键突破在于揭示“压力反增”现象的物理根源。初步理论分析表明，在平流层正温度梯度（温度随高度升高）驱动下，向下弯曲的射线管发生汇聚，截面积收缩，导致声压能量密度不降反升，出现局部过压峰值超过近场初始值的反增现象。本研究将基于增广Burgers方程，引入几何扩散修正项 J−1/2J−1/2，量化汇聚效应与耗散效应的竞争关系，给出压力反增发生的临界条件（包括马赫数、飞行高度、大气温度梯度的阈值组合）。同时，针对25km以上高空CO₂和H₂O分子弛豫吸收的频散特性，建立分层介质中非线性系数与吸收系数的垂向分布函数，揭示激波-膨胀波交替结构在正梯度环境下的非对称衰减规律——即激波面因汇聚而强化、膨胀波因耗散而钝化的差异化演化路径。
#### 大气风效应对高超声速波系衰减的影响规律
有风会有熵梯度
大气风场对高超声速声爆传播的影响远非简单的“对流输运”所能概括。本研究拟从“风剪切-激波相互作用”的角度，系统研究风效应对波系衰减的调制机制。具体而言，存在背景风时，大气介质处于非均匀运动状态，声爆传播的相对速度需以声速与风速矢量的合成速度为准，这导致两个重要后果：其一，顺风与逆风条件下射线路径的不对称弯曲，使地面声爆毯的形态发生系统性偏转；其二，风速的垂向剪切（∂U/∂z∂U/∂z）将改变激波面的局部倾角，进而调制波系在分层大气中的折射行为。

更为深层的问题在于有风大气中熵梯度的产生。当声爆波系通过存在水平风速梯度的区域时，非等熵压缩过程会在波后遗留熵扰动，该熵扰动与背景风场耦合，可能引发激波强度的额外耗散或局部放大。本研究拟采用线性化欧拉方程结合射线追踪方法，将风场作为背景状态量耦合进传播方程，重点分析：（1）高空急流层（~20-30km）的强风剪切带对声爆射线的偏折阈值效应；（2）顺风/逆风条件下波系衰减率的不对称性，揭示风场诱导的“衰减增强”或“衰减抑制”窗口，为特定航向下的地面噪声评估提供修正依据。
#### 近地面大气边界层对高超声速波系衰减的影响规律
近地面大气边界层（通常指地面至约1km高度）是声爆到达地面前的“最后一公里”，其湍流混合强烈、温度层结日变化显著、风速剖面呈对数律分布，对高超声速声爆波系具有独特的衰减与畸变效应。尽管声爆在到达边界层顶部时其宏观波形已基本稳定，但边界层的温度逆温和强风剪切会改变波系最后数公里的传播路径，影响地面实测波形的到达角、峰值压力及上升时间。需指出，当前大多声爆传播模型将边界层简化为常数或线性层，这一近似对高超声速极小激波角（~10°）条件下的传播已不再成立——射线近乎水平地扫过地面时，边界层内数十米高度的温风变化足以导致宏观波形的可测畸变。

本研究拟引入大气边界层气象学中的Monin-Obukhov相似理论，构建包含稳定度参数的大气边界层温-风-湍流剖面模型，并将其作为增广Burgers方程传播路径的最末段边界条件。重点研究：（1）不同稳定度（中性/稳定/不稳定）边界层下，声爆地面波形的畸变特征及峰值过压的变化幅度；（2）边界层湍流对声爆激波前沿的“磨平”效应——湍流耗散如何影响激波上升时间这一关键噪声评估指标。本项工作的价值在于弥合“高空传播理论预测”与“地面实测信号”之间的现存偏差，为声爆地面试验的数据解释提供边界层修正方法。