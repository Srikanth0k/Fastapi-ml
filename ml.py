from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class ml(BaseModel): 
    CRIM       float64
    ZN          float64
    INDUS       float64
    CHAS        float64
    NOX         float64
    RM          float64
    AGE         float64
    DIS         float64
    RAD         int64  
    TAX         int64  
    PTRATIO     float64
    B           float64
    LSTAT       float64
    MEDV        float64
    