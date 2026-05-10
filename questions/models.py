from django.db import models


class Question(models.Model):
    COMPLEXITY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    GRADE_CHOICES = [(g, f'Grade {g}') for g in range(9, 13)]

    question_text = models.TextField()
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=1)
    topic = models.CharField(max_length=100)
    grade = models.IntegerField(choices=GRADE_CHOICES)
    complexity = models.CharField(max_length=10, choices=COMPLEXITY_CHOICES)
    chapter = models.CharField(max_length=200)
    marks = models.IntegerField(default=1)
    hint = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'english_questions'
        ordering = ['grade', 'topic', 'complexity']

    def __str__(self):
        return f"[Grade {self.grade}] [{self.topic}] {self.question_text[:60]}..."

    def to_dict(self):
        return {
            'id': self.id,
            'question_text': self.question_text,
            'options': [self.option_a, self.option_b, self.option_c, self.option_d],
            'correct_answer': self.correct_answer,
            'topic': self.topic,
            'grade': self.grade,
            'complexity': self.complexity,
            'chapter': self.chapter,
            'marks': self.marks,
            'hint': self.hint,
        }
