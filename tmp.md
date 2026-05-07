## Abstract
**Why should we do**
Developing next-generation supersonic transport (SST) is one of the most critical directions for future civil transport, but most existing SST configuration have relatively small seating capacity, which limits their commercial potential.
**How to do**
Aiming at this issue, this paper proposed a 160-seats large supersonic blended-wing-body transport (SBWB) configuration.
**What do you do**
A parametric method for SBWB is developed, and the JSGD inverse design is implemented based on this method. Subsequently, the effects of winglet length and sweep angle on sonic boom characteristics are investigated.
**what is the result**
Based on the above research, a low boom design for the 160-seats SBWB configuration is performed. The ground boom intensity value is optimized to xx PLdB. In summary, the SBWB can effectively improve passenger capacity, and demonstrates favorable feasibility in sonic boom mitigation.

## Introduction
**background of SST**
Faster travel speed is an eternal pursuit of humanity. Compared with conventional subsonic airliners, SST achieve a higher cruise speed. This remarkably improves travel efficiency and facilitates global economic and cultural communication. Over the past few decades, researchers have made considerable efforts to advance the next generation of SST.

**Sonic boom: the critical barrier**
- 声爆是SST商业化的核心障碍——FAA/ICAO陆上超声速飞行禁令
- 低声爆设计是下一代SST的硬需求（NASA X-59 Quesst、JAXA D-SEND等项目背景）
- 低声爆与高气动效率之间的设计矛盾（长细比 vs 体积效率）

**Capacity limitation of current low-boom configurations**
- 现有低声爆构型（X-59、JAXA低音爆概念等）载客量普遍偏小（<50座）
- 低声爆要求细长机身 → 客舱体积受限 → 商业经济性不足
- 点出gap：大载客量与低声爆的兼容性，尚缺乏系统研究

**BWB as a potential solution**
- BWB布局提升客舱容积效率的潜力（翼身融合增加可用空间）
- BWB在超声速下的气动优势（升力面与机身一体化，减小浸润面积）
- 超声速BWB的研究现状（列举已有文献，指出研究多集中于小型/无人构型）
- 大载客量BWB低声爆设计的可行性未知 → 本文要回答这个问题

**JSGD inverse design for low-boom shaping**
- JSGD理论简述：基于等效截面积分布→远场声爆信号的关系
- JSGD给出低声爆目标的等效截面积分布
- 面向BWB的JSGD反设计难点：客舱体积硬约束导致等效截面积难以匹配目标
- 已有JSGD应用研究（列举），大BWB上的应用尚属空白

**Geometry parameterization for large design spaces**
- 大BWB设计变量维数高，传统FFD直接优化易产生奇异外形
- CST参数化方法的优势（少变量控制光滑外形）
- 参数化方法与代理优化（Kriging等）的衔接需求
- 引出本文的参数化策略：CST降维 + 参数叠加

**Winglet and afterbody flow physics**
- 翼梢小翼/后体区域对声爆的调控机理（过膨胀、激波反射）
- 已有的翼梢装置声爆研究概述
- BWB后体波系复杂性：机身末端激波 + 机翼膨胀波 + 平尾反射的耦合
- 对BWB后体波系的系统分析尚不充分

**Research objectives and contributions**
- 本文目标：探究160座级大型BWB低声爆设计的可行性
- 贡献1：提出面向大BWB的CST参数化+参数叠加几何建模策略
- 贡献2：在严格客舱体积约束下实施JSGD反设计，揭示体积-声爆矛盾的定量特征
- 贡献3：系统分析BWB后体波系结构，评估翼梢小翼对声爆的调控效果
- 贡献4：给出160座SBWB低声爆方案的可行性结论

**Paper organization**
- Section 2: 几何参数化方法（CST + 参数叠加 + 降维策略）
- Section 3: 气动与声爆分析方法（面元法/JSGD/SU2 Euler/后体波系分析）
- Section 4: 优化问题建模（设计变量、约束、目标函数）
- Section 5: 结果与讨论（基准构型声爆特征、JSGD反设计结果、翼梢小翼参数影响、最终低声爆方案）
- Section 6: 结论