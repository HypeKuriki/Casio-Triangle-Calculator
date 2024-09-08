import math

def degrees(x):
    return x * 180 / math.pi

def radians(x):
    return x * math.pi / 180

def fall_1(a, b, c):  # SSS
    alpha = degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    beta = degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    gamma = 180 - alpha - beta
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return a, b, c, alpha, beta, gamma, area

def fall_2(a, b, alpha):  # SSA
    alpha_rad = radians(alpha)
    sin_alpha = math.sin(alpha_rad)
    sin_beta = b * sin_alpha / a
    beta = degrees(math.asin(sin_beta))
    gamma = 180 - alpha - beta
    sin_gamma = math.sin(radians(gamma))
    c = a * sin_gamma / sin_alpha
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_3(a, b, beta):  # SSA
    beta_rad = radians(beta)
    sin_beta = math.sin(beta_rad)
    sin_alpha = a * sin_beta / b
    alpha = degrees(math.asin(sin_alpha))
    gamma = 180 - alpha - beta
    sin_gamma = math.sin(radians(gamma))
    c = a * sin_gamma / sin_alpha
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_4(a, c, alpha):  # SSA
    alpha_rad = radians(alpha)
    sin_alpha = math.sin(alpha_rad)
    sin_beta = c * sin_alpha / a
    beta = degrees(math.asin(sin_beta))
    gamma = 180 - alpha - beta
    sin_gamma = math.sin(radians(gamma))
    b = a * sin_beta / sin_alpha
    area = 0.5 * a * c * sin_beta
    return a, b, c, alpha, beta, gamma, area

def fall_5(a, c, gamma):  # SSA
    gamma_rad = radians(gamma)
    sin_gamma = math.sin(gamma_rad)
    sin_alpha = a * sin_gamma / c
    alpha = degrees(math.asin(sin_alpha))
    beta = 180 - alpha - gamma
    sin_beta = math.sin(radians(beta))
    b = a * sin_beta / sin_alpha
    area = 0.5 * a * c * sin_beta
    return a, b, c, alpha, beta, gamma, area

def fall_6(b, c, beta):  # SSA
    beta_rad = radians(beta)
    sin_beta = math.sin(beta_rad)
    sin_alpha = c * sin_beta / b
    alpha = degrees(math.asin(sin_alpha))
    gamma = 180 - alpha - beta
    sin_gamma = math.sin(radians(gamma))
    a = b * sin_gamma / sin_beta
    area = 0.5 * b * c * sin_alpha
    return a, b, c, alpha, beta, gamma, area

def fall_7(b, c, gamma):  # SSA
    gamma_rad = radians(gamma)
    sin_gamma = math.sin(gamma_rad)
    sin_beta = b * sin_gamma / c
    beta = degrees(math.asin(sin_beta))
    alpha = 180 - beta - gamma
    sin_alpha = math.sin(radians(alpha))
    a = b * sin_alpha / sin_beta
    area = 0.5 * b * c * sin_alpha
    return a, b, c, alpha, beta, gamma, area

def fall_8(a, b, gamma):  # SAS
    gamma_rad = radians(gamma)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(gamma_rad))
    alpha = degrees(math.asin(a * math.sin(gamma_rad) / c))
    beta = 180 - gamma - alpha
    area = 0.5 * a * b * math.sin(gamma_rad)
    return a, b, c, alpha, beta, gamma, area

def fall_9(a, c, beta):  # SAS
    beta_rad = radians(beta)
    b = math.sqrt(a**2 + c**2 - 2 * a * c * math.cos(beta_rad))
    alpha = degrees(math.asin(a * math.sin(beta_rad) / b))
    gamma = 180 - alpha - beta
    area = 0.5 * a * c * math.sin(beta_rad)
    return a, b, c, alpha, beta, gamma, area
