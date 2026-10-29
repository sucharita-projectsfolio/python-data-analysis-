import math

class DataAnalyzer:
    def __init__(self, data):
        self.data = [float(x) for x in data]

    def get_summary(self):
        n = len(self.data)
        mean = sum(self.data) / n
        variance = sum((x - mean) ** 2 for x in self.data) / (n - 1) if n > 1 else 0.0
        return {"count": n, "mean": round(mean, 4), "std_dev": round(math.sqrt(variance), 4), "min": min(self.data), "max": max(self.data)}

if __name__ == "__main__":
    print(DataAnalyzer([12.4, 14.5, 13.8, 15.2, 14.9, 13.1, 16.0]).get_summary())
