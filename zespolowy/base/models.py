from django.db import models
from django.contrib.auth.models import User

lvl1 = 10
lvl2 = 20
lvl3 = 40
lvl4 = 60

exp_levels = (
    (lvl1, 'Easy'),
    (lvl2, 'Average'),
    (lvl3, 'Complex'),
    (lvl4, 'BOSS'),
)


class task(models.Model):
    # na czas testow/prod null i blank = True

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    complete = models.BooleanField(default=False)
    exp = models.IntegerField(choices=exp_levels, default=lvl1, null=True, blank=True)
    dateTime_created = models.DateTimeField(auto_now_add=True) # auto_now_add ustawia timestamp jako datę utworzenia, kalendarz dodać puzniej

    def __str__(self):
        return str(self.title + ' ' + self.description)

    class Meta:
        ordering = ['complete']