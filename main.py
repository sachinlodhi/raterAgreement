from sklearn.metrics import cohen_kappa_score
import random

# number of criteria
criterion = 7
threshold = 0.7

for i in range(1000):
    # number of raters [currently only 2 raters] these raters can be changed in the future
    # but as of now in my opinion the Cohen's kappa score works between only 2 raters
    rater1 = [random.randint(0, 1) for j in range(criterion)]
    rater2 = [random.randint(0, 1) for j in range(criterion)]
    ans = cohen_kappa_score(rater1, rater2)
    if ans>threshold:
        print(rater1)
        print(rater2)
        print(ans)


