---
tags:
- autonomy
- adaptability
- efficiency
- supervise
- unsupervise
- inductive
- learning
---

# What is Machine Learning?

- A computer program that improves its performance at some task through experience.


## Subfields of ML

1. Supervised Learning
    - Decision Tree

2. Unsupervised Learning

3. Reinforced Learning

## Decision Tree

How do we *supervise* the algorithm?  What does it mean to *supervise*?  Supervision here means we provide a set of examples and the algorithm will use this set to produce predictions.

First, we need to describe the *features*/attributes of the data set, i.e. *data representation*.  In the case of CSV format, the *feature values* are represented in comma-separated values.

**Note:** the concept of *noise* will be discussed more in the future.  In brief, noise could appear as inaccurate labeling of data, for example.

## The Induction Framework

1. Traning Data
2. Learning Algorithm
3. f
4. Test Example

```txt
1 -> 2 -> 3 <-> 4 -> 3
    
f(x) -> y
    where
        x: examples
	    y: label
```

## Types of Inductive Learning

1. Regression
2. Binary classification
3. Multiclass classification
4. Discovery
5. Reinforced learning

*We focus on 1-4 for now.*

$f(x) \to R^+$
$f(x) \to {0, 1} {+, -}$
$f(x) \to { NYC, SF, Pullman, CA }$

## Prediction Accuracy

$$Accuracy  = \frac {\#correct}{\#total}$$

## Performance: Loss Function

- `L(., .)`
    ```tex
    L(y, $y^$)
        where
            y  = true label
            $y^$ = 
    ```

- Regression
- Binary classif.
- Multiclass classsif.
- Discovery
- Reinforcement learning
