import math

def degrees(x):
    return x * 180 / math.pi

def radians(x):
    return x * math.pi / 180

def fall_10(b, c, alpha):  # SAS
    alpha_rad = radians(alpha)
    a = math.sqrt(b**2 + c**2 - 2 * b * c * math.cos(alpha_rad))
    beta = degrees(math.asin(b * math.sin(alpha_rad) / a))
    gamma = 180 - alpha - beta
    area = 0.5 * b * c * math.sin(alpha_rad)
    return a, b, c, alpha, beta, gamma, area

def fall_11(a, alpha, beta):  # AAS
    gamma = 180 - alpha - beta
    sin_alpha = math.sin(radians(alpha))
    sin_beta = math.sin(radians(beta))
    sin_gamma = math.sin(radians(gamma))
    b = a * (sin_beta / sin_alpha)
    c = a * (sin_gamma / sin_alpha)
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_12(a, alpha, gamma):  # AAS
    beta = 180 - alpha - gamma
    sin_alpha = math.sin(radians(alpha))
    sin_beta = math.sin(radians(beta))
    sin_gamma = math.sin(radians(gamma))
    b = a * (sin_beta / sin_alpha)
    c = a * (sin_gamma / sin_alpha)
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_13(a, beta, gamma):  # AAS
    alpha = 180 - beta - gamma
    sin_alpha = math.sin(radians(alpha))
    sin_beta = math.sin(radians(beta))
    sin_gamma = math.sin(radians(gamma))
    b = a * (sin_beta / sin_alpha)
    c = a * (sin_gamma / sin_alpha)
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_14(b, alpha, beta):  # AAS
    gamma = 180 - alpha - beta
    sin_alpha = math.sin(radians(alpha))
    sin_beta = math.sin(radians(beta))
    sin_gamma = math.sin(radians(gamma))
    a = b * (sin_alpha / sin_beta)
    c = b * (sin_gamma / sin_beta)
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_15(b, alpha, gamma):  # AAS
    beta = 180 - alpha - gamma
    sin_alpha = math.sin(radians(alpha))
    sin_beta = math.sin(radians(beta))
    sin_gamma = math.sin(radians(gamma))
    a = b * (sin_alpha / sin_beta)
    c = b * (sin_gamma / sin_beta)
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_16(b, beta, gamma):  # AAS
    alpha = 180 - beta - gamma
    sin_alpha = math.sin(radians(alpha))
    sin_beta = math.sin(radians(beta))
    sin_gamma = math.sin(radians(gamma))
    a = b * (sin_alpha / sin_beta)
    c = b * (sin_gamma / sin_beta)
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_17(c, alpha, beta):  # AAS
    gamma = 180 - alpha - beta
    sin_alpha = math.sin(radians(alpha))
    sin_beta = math.sin(radians(beta))
    sin_gamma = math.sin(radians(gamma))
    a = c * (sin_alpha / sin_gamma)
    b = c * (sin_beta / sin_gamma)
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_18(c, alpha, gamma):  # AAS
    beta = 180 - alpha - gamma
    sin_alpha = math.sin(radians(alpha))
    sin_beta = math.sin(radians(beta))
    sin_gamma = math.sin(radians(gamma))
    a = c * (sin_alpha / sin_gamma)
    b = c * (sin_beta / sin_gamma)
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area

def fall_19(c, beta, gamma):  # AAS
    alpha = 180 - beta - gamma
    sin_alpha = math.sin(radians(alpha))
    sin_beta = math.sin(radians(beta))
    sin_gamma = math.sin(radians(gamma))
    a = c * (sin_alpha / sin_beta)
    b = c * (sin_gamma / sin_beta)
    area = 0.5 * a * b * sin_gamma
    return a, b, c, alpha, beta, gamma, area
