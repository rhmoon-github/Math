"""
线性规划示例
支持使用 scipy、pulp 和 cvxpy 三种方式进行线性规划计算
"""

import numpy as np
from scipy.optimize import linprog
import pulp
import cvxpy as cp


def example_scipy():
    """使用 scipy.optimize.linprog 求解线性规划问题
    
    示例问题：
    最大化: z = 1300000 x1 + 600000 x2 + 500000 x3
    约束条件:
        300000 x1 + 150000 x2 + 100000 x3 <= 4000000
        90000 x1 + 30000 x2 + 40000 x3 <= 1000000
        x1 <= 5
        x1, x2, x3 >= 0
    """
    print("=" * 50)
    print("使用 scipy.optimize.linprog 求解")
    print("=" * 50)
    
    # 目标函数系数（注意：linprog 默认求最小值，所以取负号）
    c = [-1300000, -600000, -500000]  # 负号因为要最大化
    
    # 不等式约束矩阵 A_ub * x <= b_ub
    A_ub = [
        [300000, 150000, 100000],  # 约束1
        [90000, 30000, 40000],     # 约束2
        [1, 0, 0]                  # 约束3: x1 <= 5
    ]
    b_ub = [4000000, 1000000, 5]
    
    # 变量边界
    bounds = [(0, None), (0, None), (0, None)]
    
    # 求解
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    
    if result.success:
        print(f"最优解: x1 = {result.x[0]:.2f}, x2 = {result.x[1]:.2f}, x3 = {result.x[2]:.2f}")
        print(f"最优值: z = {-result.fun:.2f}")  # 取负号还原最大值
    else:
        print("求解失败:", result.message)


def example_pulp():
    """使用 PuLP 求解线性规划问题
    
    示例问题：
    最大化: z = 1300000 x1 + 600000 x2 + 500000 x3
    约束条件:
        300000 x1 + 150000 x2 + 100000 x3 <= 4000000
        90000 x1 + 30000 x2 + 40000 x3 <= 1000000
        x1 <= 5
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
    prob += 1300000*x1 + 600000*x2 + 500000*x3, "目标函数"
    
    # 约束条件
    prob += 300000*x1 + 150000*x2 + 100000*x3 <= 4000000, "约束1"
    prob += 90000*x1 + 30000*x2 + 40000*x3 <= 1000000, "约束2"
    prob += x1 <= 5, "约束3"
    
    # 求解
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    
    # 输出结果
    print(f"状态: {pulp.LpStatus[prob.status]}")
    if prob.status == pulp.LpStatusOptimal:
        print(f"最优解: x1 = {x1.varValue:.2f}, x2 = {x2.varValue:.2f}, x3 = {x3.varValue:.2f}")
        print(f"最优值: z = {pulp.value(prob.objective):.2f}")


def example_cvxpy():
    """使用 CVXPY 求解线性规划问题
    
    示例问题：
    最大化: z = 1300000 x1 + 600000 x2 + 500000 x3
    约束条件:
        300000 x1 + 150000 x2 + 100000 x3 <= 4000000
        90000 x1 + 30000 x2 + 40000 x3 <= 1000000
        x1 <= 5
        x1, x2, x3 >= 0
    """
    print("\n" + "=" * 50)
    print("使用 CVXPY 求解")
    print("=" * 50)
    
    # 创建变量
    x = cp.Variable(3, nonneg=True)
    
    # 目标函数
    objective = cp.Maximize(1300000*x[0] + 600000*x[1] + 500000*x[2])
    
    # 约束条件
    constraints = [
        300000*x[0] + 150000*x[1] + 100000*x[2] <= 4000000,
        90000*x[0] + 30000*x[1] + 40000*x[2] <= 1000000,
        x[0] <= 5
    ]
    
    # 创建问题并求解
    prob = cp.Problem(objective, constraints)
    prob.solve()
    
    # 输出结果
    if prob.status == 'optimal':
        print(f"最优解: x1 = {x.value[0]:.2f}, x2 = {x.value[1]:.2f}, x3 = {x.value[2]:.2f}")
        print(f"最优值: z = {prob.value:.2f}")
    else:
        print(f"求解状态: {prob.status}")


if __name__ == "__main__":
    print("线性规划计算示例\n")
    
    # 运行三种方法的示例
    try:
        example_scipy()
    except Exception as e:
        print(f"scipy 示例出错: {e}")
    
    try:
        example_pulp()
    except Exception as e:
        print(f"pulp 示例出错: {e}")
    
    try:
        example_cvxpy()
    except Exception as e:
        print(f"cvxpy 示例出错: {e}")

