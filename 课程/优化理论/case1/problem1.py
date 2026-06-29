import numpy as np

rho = 1.23
mu = 17.8e-6
V = 35
S = 11.8
S_wet = 2.05*S
k = 1.2
C_L = 0.3
e = 0.96

global exam_count
exam_count = 0

def CD(A):
    global exam_count
    ## 计算bc, A = b**2/S, S = bc
    b = np.sqrt(A*S)
    c = S/(b+1e-13)

    ## C_f
    Re = (rho*V*c)/mu
    C_f = 0.074/(Re**0.2)
    
    Cd = k * C_f * (S_wet/S) + C_L**2/(np.pi*(A+1e-13)*e)

    exam_count += 1

    return Cd

## 黄金分割法
def golden(f, bounds):
    ## 初始化
    g = (np.sqrt(5) - 1)/2
    ε = 1e-6
    a, b = bounds[0], bounds[1]

    x1, x2 = a+(1-g)*(b-a), a+g*(b-a)
    candidate = [f(a), f(x1), f(x2), f(b)]
    flag = 0

    for i in range(100):
        if abs(a - b) < ε:
            flag = 1

        if candidate[1] > candidate[2]:
            if flag == 1:
                optfun = candidate[2]
                optvar = x2
                break
            candidate[1] = candidate[2]
            a = a+(1-g)*(b-a)
            x2 = a+g*(b-a)
            candidate[2] = f(x2)
        else:
            if flag == 1:
                optfun = candidate[1]
                optvar = x1
                break
            candidate[2] = candidate[1]
            b = a+g*(b-a)
            x1 = a+(1-g)*(b-a)
            candidate[1] = f(x1)

    print(f"迭代{i+1}次")

    return optvar, optfun

def grad(f, *args):
    eps = 1e-6
    args_pert = list(args)
    args_pert[0] += eps
    return (f(*args_pert) - f(*args)) / eps

## 回溯算法
def Backtrack(f, x0):
    x = x0; a0 = 1
    maxiter = 100
    for i in range(maxiter):
        g = grad(f, x)
        if np.linalg.norm(g) < 1e-10:
            break
        p = - g/(np.linalg.norm(g))
        a = a0; back_ratio = 0.3; mu1 = 1e-4
        for _ in range(10):
            new_x = x + a*p
            if f(new_x) <= f(x) + mu1*a*g*p:
                x = new_x
                break
            else:
                a = back_ratio*a
        
    print(f"迭代{i+1}次")

    return x, f(x)

## 调用Wolfe算法求步长的简单梯度优化
def simple_grad_opt(f, x0):
    x = x0
    maxiter = 100
    for i in range(maxiter):
        g = grad(f, x)
        if np.linalg.norm(g) < 1e-10:
            break
        p = - g/(np.linalg.norm(g))
        a = Wolfe(f, x, p)
        x = x + a*p

    print(f"迭代{i+1}次")

    return x, f(x)

def Wolfe(f, x, p):
    mu1 = 1e-4; mu2 = 0.9; amax = 10
    ## 定义phi函数
    def phi(a):
        new_x = x + a*p
        return f(new_x)
    
    pphi0 = grad(phi, 0)
    def zoom(alo, ahi):
        for i in range(100):
            aj = 0.5*(alo+ahi)
            tmp = phi(aj)
            if tmp > phi(0)+mu1*aj*pphi0 or tmp>phi(alo):
                ahi = aj
                continue
            pphi = grad(phi, aj)
            if abs(pphi) <= -mu2*pphi0:
                a = aj
                return a
            
            if pphi*(ahi - alo) >= 0:
                ahi = alo; alo = aj
                continue
            else:
                alo = aj
                continue
    
    maxiter = 100
    a = np.zeros(100)
    a[0] = 0; a[1] = 1
    target_a = a[1]
    for i in range(1, maxiter):
        if (phi(a[i]) > phi(0) + mu1*a[i]*pphi0
            ) or (phi(a[i])>phi(a[i-1]) and i>1):
            return zoom(a[i-1], a[i])
        
        pphi = grad(phi, a[i])
        if abs(pphi) <= -mu2*pphi0:
            return a[i]
        
        if pphi > 0:
            return zoom(a[i-1], a[i])
        
        a[i+1] = 2*a[i]

    return target_a

if __name__ == "__main__":
    A0 = 0.1
    bounds = (0, 100)
    print(golden(CD, bounds))
    print(Backtrack(CD, A0))
    print(simple_grad_opt(CD, A0))
    print(f"函数评估次数{exam_count}")