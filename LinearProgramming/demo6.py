"""
线性规划示例
支持使用 scipy、pulp 和 cvxpy 三种方式进行线性规划计算
"""

import pulp



def example_pulp():
    """使用 PuLP 求解线性规划问题
    
    示例问题：
    最小化: z = 700*x1 + 900*x2 + 800*x3 + 800*x4 + 900*x5 + 700*x6
    约束条件:
        x1 + x2 + x3 = 12
        x4 + x5 + x6 = 15
        x1 + x4 <= 10
        x2 + x5 <= 8
        x3 + x6 <= 9
        x1, x2, x3, x4, x5, x6 >= 0
    """
    print("\n" + "=" * 50)
    print("使用 PuLP 求解")
    print("=" * 50)
    
    # 创建问题
    prob = pulp.LpProblem("线性规划示例", pulp.LpMinimize)
    
    # 创建变量
    x1 = pulp.LpVariable("x1", lowBound=0, cat='Continuous')
    x2 = pulp.LpVariable("x2", lowBound=0, cat='Continuous')
    x3 = pulp.LpVariable("x3", lowBound=0, cat='Continuous')
    x4 = pulp.LpVariable("x4", lowBound=0, cat='Continuous')
    x5 = pulp.LpVariable("x5", lowBound=0, cat='Continuous')
    x6 = pulp.LpVariable("x6", lowBound=0, cat='Continuous')
    
    # 目标函数
    prob += 700*x1 + 900*x2 + 800*x3 + 800*x4 + 900*x5 + 700*x6, "目标函数"
    
    # 约束条件
    prob += x1 + x2 + x3 == 12, "约束1"
    prob += x4 + x5 + x6 == 15, "约束2"
    prob += x1 + x4 <= 10, "约束3"
    prob += x2 + x5 <= 8, "约束4"
    prob += x3 + x6 <= 9, "约束5"

    
    # 求解
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    
    # 输出结果
    print(f"状态: {pulp.LpStatus[prob.status]}")
    if prob.status == pulp.LpStatusOptimal:
        print(f"最优解: x1 = {x1.varValue:.2f}, x2 = {x2.varValue:.2f}, x3 = {x3.varValue:.2f}, "
              f"x4 = {x4.varValue:.2f}, x5 = {x5.varValue:.2f}, x6 = {x6.varValue:.2f}")
        print(f"最优值: z = {pulp.value(prob.objective):.2f}")
    elif prob.status == pulp.LpStatusUnbounded:
        print("问题无界：可能是约束条件不足或目标函数设置错误")
    elif prob.status == pulp.LpStatusInfeasible:
        print("问题无可行解：约束条件相互矛盾")



if __name__ == "__main__":
    print("线性规划计算示例\n")
    
    try:
        example_pulp()
    except Exception as e:
        print(f"pulp 示例出错: {e}")

