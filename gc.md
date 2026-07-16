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
声爆研究可追溯到上世纪六十年代，早期学者集中于研究标准“N“型波，认为飞行器外形仅能改变N波的幅值，基于这种思想Jones根据Whitham理论给出了使N波幅值最小的F函数形式。
70年代学者发现对于机身较长的飞行器，其声爆传播到地面可以保持为不完全合并的中场波系形态，人们开始关注近场波形对传播中合并的影响，在这种思想的引导下Jones，Seebass，George，Darden等人基于Whitham理论推导出了经典的声爆最小化理论，该理论指出通过改变外形调控近场波系可使地面声爆信号呈现斜坡状形态，这种形态的地面信号声爆强度远低于N波，该理论时至今日依然是低声爆概念设计阶段的重要思想。
之后的几十年里随着计算机技术的发展，使用CFD技术直接计算高可信度的声爆信号成为可能，通过现代优化手段和高可信度声爆分析，发展了更先进的低声爆设计方法，进一步突破了JSGD指导的声爆下限，其中代表性的就是声爆强度低于75PLdB的X-59试验机，其近场声爆形态与JSGD理论差异甚大也可说明对近场波系形态的理解得到了长足的发展。
CFD技术发展带来的不仅是更好的近场波系形态的探索，还有对速度边界的延拓，部分学者开始关注高超声速飞机的声爆，一方面在40km研究表明高超声速条件下修正线化理论等声爆解析方法均不再适用，为此，针对高超条件的声爆研究具备了必要性，然而受限于高超声速流场的复杂性，现有的研究主要集中于对简单N波幅值的研究。
回顾声爆研究的几十年历程，正是从N波幅值的研究到调控近场波系形态的思想跃迁催生了超声速民机低声爆设计技术的快速发展，有鉴于此可以合理推测，高超声速条件下近场波系形态的演化机理研究必然能够指导高超声速民机低声爆设计技术的发展。
$$\left(1-M_{ref}^{2}\right)\frac{\partial^{2}\phi}{\partial x^{2}}+\frac{\partial^{2} \phi}{\partial y^{2}}+\frac{\partial^{2} \phi}{\partial z^{2}}=\frac{M_{ref}^{2}(\gamma+1)}{u_{ref}} \frac{\partial \phi}{\partial x}$$
    
- whitham理论中aging（波形老化，实际上就是合并抵消畸变衰减一系列行为的总称）的概念，特征线的概念

参考文献：

	[1] Yamashita
计算了旋成体在高超声速条件下的声爆特性，均匀大气马赫7和真实大气马赫5以下波形参数法与CFD结果基本吻合，Whitham理论有误差，<**现有快速方法仅能覆盖到5马赫**><**高空高超的声爆显著低于中超声速**>

	[2]Simplification of Numerical and Analytical Tools for Sonic Boom Description
<说是有中场的计算，但是查不到这篇>

	[3] Russo G, Voto C, Savino R. S4 - A demonstrator of HYPLANE, a single stage suborbital spaceplane and a hypersonic business jet[J]. Acta Astronautica, 2021, 183:244-254. [https://doi.org/10.1016/j.actaastro.2021.03.025](https://link.wtturl.cn/?target=https%3A%2F%2Fdoi.org%2F10.1016%2Fj.actaastro.2021.03.025&scene=im&aid=582478&lang=zh "autolink").
S4的HYPLANE项目，已有的商用高超方案，目前用不到
文章阐释了小型商用高超的优势

	[4]Sippel M，Callsen S，Singh S，等. SpaceLiner: the 2025 pre-definition status report[J/OL]. CEAS Space Journal，2026-05-05. [https://doi.org/10.1007/s12567-026-00727-x](https://doi.org/10.1007/s12567-026-00727-x). DOI:[10.1007/s12567-026-00727-x](https://doi.org/10.1007/s12567-026-00727-x).
高超火箭

	[5]Darden C M. Sonic boom theory: its status in prediction and minimization[J]. Journal of Aircraft, 1977, 14(6): 569-576.
综述声爆发展，完善SG方法，考虑文献较早，综述只做参考

	[6]Callsen S, Wilken J, Sippel M. Analysis of sonic boom propagation and population disturbance of hypersonic vehicle trajectories: S. Callsen et al[J]. CEAS Space Journal, 2025, 17(5): 797-814.
高超声爆研究，不过主要规避策略是跳出大气层

	[7]Bishop J W, Blom P, Carr C, et al. An infrasound source analysis of the OSIRIS-REx sample return capsule hypersonic re-entry[J]. The Journal of the Acoustical Society of America, 2025, 158(6): 4637-4650.
没找到全文，算的是探测器返回舱的声爆，作为高超N波研究的支撑文献吧

	[8]Graziani S, Jäschke J J, Viola N, et al. Sonic Boom Velocity and Altitude Sensitivity Analysis of a Hypersonic Aircraft Concept[J]. SAE International Journal of Advances and Current Practices in Mobility 306418, 2025, 7(6): 2940-2953.
比较正统的高超声爆研究，研究速度和高度的影响，覆盖了1.2-5马赫（话说这也算高超？），可用于高超N波研究的支撑或者说明5马赫以上现有方法难以适用？

	[9]KING C B, SKOWRON S, MILLER S A E. Fully parabolized hypersonic sonic boom prediction with real gas and viscous effects[J]. AIAA Journal, 2024, 62(5): 1683-1700.
考虑真实气体和黏性效应的高超声爆CFD方法，可以支撑高超现有方法不适用的观点
计算范围覆盖4-15马赫（这才是真高超啊）

	[10]Parametric Study of the Hypersonic Near-Field and Sonic Boom from Waveriders using a Fully-Parabolized Approach
	[11]Computational and experimental investigation of near-field sonic boom of a HTV-2 type hypersonic boost gliding vehicle
	[12]Rapid hypersonic sonic boom prediction using line-distributed energy impulse formulations with and without lift effect

### 研究内容

- 主要研究非均匀大气的影响
    
    - 主要研究非均匀大气的影响
        
    - 大气边界层效应的影响
        
    - 地面传播中的激波演化过程

### 研究方案