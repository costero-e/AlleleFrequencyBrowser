from django import forms

class BamForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BamForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
    choices_genome = [("hg38", "hg38"), ("hg37", "hg37"), ("NCBI36", "NCBI36")]
    choices_cohort = [("GDI", "GDI")]
    mutated_allele = forms.CharField(max_length=50, required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'Search for a variant (e.g.  13-32398489-A-T)', 'size':40}))
    genome = forms.ChoiceField(choices=choices_genome, help_text="<span class='hovertext' data-hover='Name of the genome to be queried'>Reference</span>", label="")
    cohort = forms.ChoiceField(choices=choices_cohort, help_text="<span class='hovertext' data-hover='Name of the genome to be queried'>Reference</span>", label="")

