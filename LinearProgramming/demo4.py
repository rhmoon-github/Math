"""
线性规划示例
支持使用 scipy、pulp 和 cvxpy 三种方式进行线性规划计算
"""

import numpy as np
from scipy.optimize import linprog
import pulp
import cvxpy as cp



def example_pulp():
    """使用 PuLP 求解线性规划问题
    
    示例问题：
    最大化: z = 45 x1 + 70 x2 + 50 x3
    约束条件:
        40 x1 + 80 x2 + 90 x3 <= 25
        100 x1 + 160 x2 + 140 x3 <= 45
        190 x1 + 240 x2 + 160 x3 <= 65
        200 x1 + 310 x2 + 220 x3 <= 80
        x1 <= 1
        x2 <= 1
        x3 <= 1
        x1, x2, x3 >= 0
    """
    print("\n" + "=" * 50)
    print("使用 PuLP 求解")
    print("=" * 50)
    
    # 创建问题
    prob = pulp.LpProblem("线性规划示例", pulp.LpMaximize)
    
    # 创建变量
    x1 = pulp.LpVariable("x1", lowBound=0, cat='Continuous')
    x2 = pulp.LpVariable("x2", lowBound=0, cat='Continuous')
    x3 = pulp.LpVariable("x3", lowBound=0, cat='Continuous')
    
    # 目标函数
    prob += 45*x1 + 70*x2 + 50*x3, "目标函数"
    
    # 约束条件
    prob += 40*x1 + 80*x2 + 90*x3 <= 25, "约束1"
    prob += 100*x1 + 160*x2 + 140*x3 <= 45, "约束2"
    prob += 190*x1 + 240*x2 + 160*x3 <= 65, "约束3"
    prob += 200*x1 + 310*x2 + 220*x3 <= 80, "约束4"
    prob += x1 <= 1, "约束5"
    prob += x2 <= 1, "约束6"
    prob += x3 <= 1, "约束7"
    
    # 求解
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    
    # 输出结果
    print(f"状态: {pulp.LpStatus[prob.status]}")
    if prob.status == pulp.LpStatusOptimal:
        print(f"最优解: x1 = {x1.varValue:.2f}, x2 = {x2.varValue:.2f}, x3 = {x3.varValue:.2f}")
        print(f"最优值: z = {pulp.value(prob.objective):.2f}")



if __name__ == "__main__":
    print("线性规划计算示例\n")
    
    try:
        example_pulp()
    except Exception as e:
        print(f"pulp 示例出错: {e}")

