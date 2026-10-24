from django import forms

class PlaceForm(forms.Form):
    PLACE_CHOICES = [
        ('Ресторан', 'Ресторан'),
        ("Кав'ярня", "Кав'ярня"),
        ('Парк', 'Парк / Прогулянка'),
        ('Розваги', 'Розваги'),
        ('Інше', 'Інше'),
    ]

    title = forms.CharField(
        label='Назва місця',
        max_length=120,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад: Львівські круасани'}),
    )

    place_type = forms.ChoiceField(
        label='Тип місця',
        choices=PLACE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    location = forms.CharField(
        label='Локація',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Залиште порожнім, якщо це таємне місце'}),
    )

    rating = forms.IntegerField(
        label='Ваш рейтинг',
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
    )

    description = forms.CharField(
        label='Опис місця',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Опишіть враження від цього місця'}),
    )
