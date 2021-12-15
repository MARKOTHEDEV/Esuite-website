from django.db import models



class SolutionDetail(models.Model):
    heading = models.CharField(max_length=400)


    def __str__(self):return self.heading


class SolutionDetailParagraph(models.Model):
    paragraph = models.TextField()
    solution_detail = models.ForeignKey(SolutionDetail,on_delete=models.CASCADE)