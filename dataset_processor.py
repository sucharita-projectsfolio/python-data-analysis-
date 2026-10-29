def calculate_statistical_variance(data):
    n = len(data)
    mean = sum(data) / n
    sample_variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return {"mean": round(mean, 4), "sample_variance": round(sample_variance, 4)}

if __name__ == "__main__":
    print(calculate_statistical_variance([14.2, 15.1, 14.8, 13.9, 15.5, 14.6]))
