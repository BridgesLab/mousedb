"""This module describes the Strain, Animal, Breeding and Cage data models.

This module stores all data regarding a particular laboratory animal.  Information about experimental data and timed matings are stored in the data and timed_matings packages.  This module describes the database structure for each data model."""

from django.db import models
import datetime

GENOTYPE_CHOICES = (
	('Single Knockout',(
		('+/+', 'Wild-Type'),
		('-/+', 'Heterozygous'),
		('-/-', 'Knockout'),
        ('-/Y', 'X-Linked Knockout'),
		('N.D.', 'Not Determined')
		)
	),
	('Double Knockout', (
		('-/-; +/+', 'Knockout/Wild-Type'),
		('-/-; +/-', 'Knockout/Heterozygoous'),
		('-/-; -/-', 'Double Knockout'),
		('-/+; +/+', 'Heterozygous/Wild-Type'),
		('-/+; +/-', 'Double Heterozygous'),
		('-/+; -/-', 'Heterozygous/Knockout'),
		('+/+; +/+', 'Double Wild-Type'),
		('+/+; +/-', 'Wild-Type/Heterozygous'),
		('+/+; -/-', 'Wild-Type/Knockout'),
		)
	),
	('Floxed',(
		('fl/fl', 'Floxed'),
		('fl/+', 'Heterozygous Floxed'),
		)
),
	('Transgene',(
		('Tg/Tg', 'Homozygous Transgene'),
		('Tg/+', 'Heterozygous Transgene'),
		)
),
	('Floxed with Transgene',(
		('fl/fl; ?', 'Floxed Undetermined Transgene'),
		('fl/+; ?', 'Heterozygous Floxed, Undetermined Transgene'),		
		('fl/fl; +/+', 'Floxed no Transgene'),
		('fl/+; +/+', 'Heterozygous Floxed no Transgene'),
		('fl/fl; Tg/+', 'Floxed Heterozygous Transgene'),
		('fl/+; Tg/+', 'Heterozygous Floxed, Heterozygous Transgene'),
		('fl/fl; Tg/Tg', 'Floxed, Homozygous Transgene'),
		('fl/+; Tg/Tg', 'Heterozygous Floxed, Homozygous Transgene'),
		('+/+; Tg/+', 'Wild-Type, Heterozygous Transgene'),
		('+/+; Tg/Tg', 'Wild-Type, Homozygous Transgene'),
		('+/+; +/+', 'Wild-Type, No Transgene'),        
		)
),
 ('Double Transgene',(
                ('+/+; +/+', 'No Transgenes'),
                ('Tg/+; Tg/+', 'Both Transgenes'),
                ('Tg/+; +/+', 'First Transgene Only'),
                ('+/+; Tg/+', 'Second Transgene Only'),
                )
),
	('Single Knockout with Transgene',(
		('+/+; Tg/+', 'Wild-Type, Heterozygous Transgene'),
		('+/-; Tg/+', 'Heterozygous, Heterozygous Transgene'),		
		('-/-; Tg/+', 'Knockout, Heterozygous Transgene'), 
		('+/+; Tg/Tg', 'Wild-Type, Homozygous Transgene'),
		('+/-; Tg/Tg', 'Heterozygous, Homozygous Transgene'),		
		('-/-; Tg/Tg', 'Knockout, Homozygous Transgene'), 
		('+/+; ?', 'Wild-Type, Undetermined Transgene'),
		('+/-; ?', 'Heterozygous, Undetermined Transgene'),		
		('-/-; ?', 'Knockout, Undetermined Transgene'),     
		)
),
	('Double Knockout with Transgene', (
		('-/-; +/+; Tg/+', 'Knockout/Wild-Type/Heterozygous Transgene'),
		('-/-; +/-; Tg/+', 'Knockout/Heterozygous/Heterozygous Transgene'),
		('-/-; -/-; Tg/+', 'Double Knockout/Heterozygous Transgene'),
		('-/+; +/+; Tg/+', 'Heterozygous/Wild-Type/Heterozygous Transgene'),
		('-/+; +/-; Tg/+', 'Double Heterozygous/Heterozygous Transgene'),
		('-/+; -/-; Tg/+', 'Heterozygous/Knockout/Heterozygous Transgene'),
		('+/+; +/+; Tg/+', 'Double Wild-Type/Heterozygous Transgene'),
		('+/+; +/-; Tg/+', 'Wild-Type/Heterozygous/Heterozygous Transgene'),
		('+/+; -/-; Tg/+', 'Wild-Type/Knockout/Heterozygous Transgene'),
		('-/-; +/+; Tg/Tg', 'Knockout/Wild-Type/Homozygous Transgene'),
		('-/-; +/-; Tg/Tg', 'Knockout/Heterozygous/Homozygous Transgene'),
		('-/-; -/-; Tg/Tg', 'Double Knockout/Homozygous Transgene'),
		('-/+; +/+; Tg/Tg', 'Heterozygous/Wild-Type/Homozygous Transgene'),
		('-/+; +/-; Tg/Tg', 'Double Heterozygous/Homozygous Transgene'),
		('-/+; -/-; Tg/Tg', 'Heterozygous/Knockout/Homozygous Transgene'),
		('+/+; +/+; Tg/Tg', 'Double Wild-Type/Homozygous Transgene'),
		('+/+; +/-; Tg/Tg', 'Wild-Type/Heterozygous/Homozygous Transgene'),
		('+/+; -/-; Tg/Tg', 'Wild-Type/Knockout/Homozygous Transgene'),		
		)
	),
	('Double Knockout; Floxed with Transgene',(
		('-/-;fl/fl; ?', 'Knockout/Floxed/Undetermined Transgene'),
		('-/-;fl/fl; +/+', 'Knockout/Floxed/no Transgene'),
		('-/-;fl/+; +/+', 'Knockout/Heterozygous Floxed/ no Transgene'),
		('-/-;fl/fl; Tg/+', 'Knockout/Floxed/ Heterozygous Transgene'),
		('-/-;fl/+; Tg/+', 'Knockout/Heterozygous Floxed/ Heterozygous Transgene'),
		('-/-;fl/fl; Tg/Tg', 'Knockout/Floxed/Homozygous Transgene'),
		('-/-;fl/+; Tg/Tg', 'Knockout/Heterozygous Floxed/Homozygous Transgene'),
		('-/-;+/+; Tg/+', 'Knockout/Wild-Type/Heterozygous Transgene'),
		('-/-;+/+; Tg/Tg', 'Knockout/Wild-Type/Homozygous Transgene'),
		('+/-;fl/fl; ?', 'Heterozygote/Floxed/Undetermined Transgene'),
		('+/-;fl/fl; +/+', 'Heterozygote/Floxed/no Transgene'),
		('+/-;fl/+; +/+', 'Heterozygote/Heterozygous Floxed/no Transgene'),
		('+/-;fl/fl; Tg/+', 'Heterozygote/Floxed/ Heterozygous Transgene'),
		('+/-;fl/+; Tg/+', 'Heterozygote/Heterozygous Floxed/Heterozygous Transgene'),
		('+/-;fl/fl; Tg/Tg', 'Heterozygote/Floxed/Homozygous Transgene'),
		('+/-;fl/+; Tg/Tg', 'Heterozygote/Heterozygous Floxed/Homozygous Transgene'),
		('+/-;+/+; Tg/+', 'Heterozygote/Wild-Type/Heterozygous Transgene'),
		('+/-;+/+; Tg/Tg', 'Heterozygote/Wild-Type/Homozygous Transgene'),
		('+/-;+/+; +/+', 'Heterozygote/Wild-Type/No Transgene'),        
		('+/+;fl/fl; ?', 'Wild-Type/Floxed/Undetermined Transgene'),
		('+/+;fl/fl; +/+', 'Wild-Type/Floxed/no Transgene'),
		('+/+;fl/+; +/+', 'Wild-Type/Heterozygous Floxed/no Transgene'),
		('+/+;fl/fl; Tg/+', 'Wild-Type/Floxed/Heterozygous Transgene'),
		('+/+;fl/+; Tg/+', 'Wild-Type/Heterozygous Floxed/Heterozygous Transgene'),
		('+/+;fl/fl; Tg/Tg', 'Wild-Type/Floxed/Homozygous Transgene'),
		('+/+;fl/+; Tg/Tg', 'Wild-Type/Heterozygous Floxed/Homozygous Transgene'),
		('+/+;+/+; Tg/+', 'Wild-Type/Wild-Type/Heterozygous Transgene'),
		('+/+;+/+; Tg/Tg', 'Wild-Type/Wild-Type/Homozygous Transgene'),
        ('+/+;+/+; ?', 'Wild-Type/Wild-Type/Unknown Transgene'),
        ('+/+;+/+; +/+', 'Wild-Type/Wild-Type/No Transgene'),
		('-/Y;fl/fl; ?', 'X-Linked Knockout/Floxed/Undetermined Transgene'),
		('-/Y;fl/fl; +/+', 'X-Linked Knockout/Floxed/no Transgene'),
		('-/Y;fl/+; +/+', 'X-Linked Knockout/Heterozygous Floxed/no Transgene'),
		('-/Y;fl/fl; Tg/+', 'X-Linked Knockout/Floxed/ Heterozygous Transgene'),
		('-/Y;fl/+; Tg/+', 'X-Linked Knockout/Heterozygous Floxed/Heterozygous Transgene'),
		('-/Y;fl/fl; Tg/Tg', 'X-Linked Knockout/Floxed/Homozygous Transgene'),
		('-/Y;fl/+; Tg/Tg', 'X-Linked Knockout/Heterozygous Floxed/Homozygous Transgene'),
		('-/Y;+/+; Tg/+', 'X-Linked Knockout/Wild-Type/Heterozygous Transgene'),
		('-/Y;+/+; Tg/Tg', 'X-Linked Knockout/Wild-Type/Homozygous Transgene'),        
		('-/Y;+/+; +/+', 'X-Linked Knockout/Wild-Type/No Transgene'),          
		)
		)
	)


GENDER_CHOICES = (
('M', 'Male'),
('F', 'Female'),
('N.D.', 'Not Determined')
)

CROSS_TYPE = (
('WT vs HET', 'Backcross'),
('HET vs HET', 'Intercross'),
('KO vs HET', 'Knockout vs Heterozygote'),
('KO vs WT', 'Generate Hets'),
('WT vs WT', 'Wild-Type Only'),
('KO vs KO', 'Knockout Only'),
('FL vs FL', 'Floxed KO Cross')
)

BACKGROUND_CHOICES = (
('C57BL/6J', 'C57BL/6J'),
('C57BL/6-BA', 'C57BL/6-BA'),
('C57BL/6-LY5.2', 'C57BL/S-LY5.2'),
('BTBR','BTBR'),
('Wistar','Wistar'),
('Mixed', 'Mixed')
)

CAUSE_OF_DEATH = (
('Unknown', 'Unknown'),
('Sacrificed', 'Sacrificed'),
('Accidental', 'Accidental'),
('Estimated', 'Estimated Death')
)

class Strain(models.Model):
    """A data model describing a mouse strain.  

    This is separate from the background of a mouse.  For example a ob/ob mouse on a mixed or a black-6 background still have the same strain.  The background is defined in the animal and breeding cages.  Strain and Strain_slug are required.
    """
    Strain = models.CharField(max_length = 100)
    Strain_slug = models.SlugField(max_length = 20, help_text="Strain name with no spaces, for use in URI's")
    Source = models.TextField(max_length = 500, blank = True)
    Comments = models.TextField (max_length = 500, blank = True)

    def __unicode__(self):
        """For a Strain object, the unicode representation is the Strain field."""
        return u'%s' % self.Strain

    @models.permalink
    def get_absolute_url(self):
        """For a Strain object, the permalinked absolute url is */strain/strain-slug*."""
        return ('strain-detail', [str(self.Strain_slug)])

class Animal(models.Model):
    """A data model describing an animal.

    This data model describes a wide variety of parameters of an experimental animal.  This model is linked to the Strain.  If the parentage of a mouse is known, this can be identified (the breeding set may not be clear on this matter). Mice are automatically marked as not alive when a Death date is provided and the object is saved.  Strain, Background and Genotype are required fields.  By default, querysets are ordered first by strain then by MouseID.
    """
    MouseID = models.IntegerField(blank = True, null=True)
    Cage = models.IntegerField(blank = True, null=True)
    Rack = models.CharField(max_length = 15, blank = True)
    Rack_Position = models.CharField(max_length = 15, blank = True)
    Strain = models.ForeignKey(Strain)
    Background = models.CharField(max_length = 25, choices = BACKGROUND_CHOICES)
    Genotype = models.CharField(max_length = 15, choices = GENOTYPE_CHOICES, default = 'N.D.')
    Gender = models.CharField(max_length = 5, choices = GENDER_CHOICES, default = 'N.D.')
    Born = models.DateField(blank = True, null=True)
    Weaned = models.DateField(blank = True, null=True)
    Death = models.DateField(blank = True, null=True)
    Cause_of_Death = models.CharField(max_length = 50, choices = CAUSE_OF_DEATH, blank=True)
    Backcross = models.IntegerField(null=True, blank=True, help_text="Leave blank for mixed background")
    Generation = models.IntegerField(null=True, blank=True)
    Breeding = models.ForeignKey('Breeding', blank=True, null=True)
    Father = models.ForeignKey('Animal', null=True, blank=True, related_name='father')
    Mother = models.ForeignKey('Animal', null=True, blank=True, related_name='mother')
    Markings = models.CharField(max_length = 100, blank=True)					
    Notes = models.TextField(max_length = 500, blank=True)
    Alive = models.BooleanField(default=True)

    def __unicode__(self):
        """This defines the unicode string of a mouse.
        If a eartag is present then the string reads some_strain-Eartag #some_number. If an eartag is not present then the mouse is labelled as use some_number, where this number is the internal database identification number and not an eartag.
        """
        if self.MouseID:
            return u'%s-EarTag #%i' % (self.Strain, self.MouseID)
        elif self.id:
             return u'%s (%i)' % (self.Strain, self.id)
        else:
             return u'MOUSE'
             
    def age(self):
        """Calculates the animals age, relative to the current date (if alive) or the date of death (if not)."""
        if (self.Death != None and
            self.Born != None):
            age =  (self.Death - self.Born).days
        elif (self.Death == None and
            self.Born != None): 
            age =  (datetime.date.today() - self.Born).days
        else:   
            age = None
        return age    

    def breeding_male_location_type(self):
        """This attribute defines whether a male's current location is the same as the breeding cage to which it belongs.

        This attribute is used to color breeding table entries such that male mice which are currently in a different cage can quickly be identified.
        The location is relative to the first breeding cage an animal is assigned to."""
        try:
            self.breeding_males.all()[0].Cage
            if self.breeding_males.all()[0].Cage is not None:
                if self.Cage is not None:
                    if self.breeding_males.all()[0].Cage == int(self.Cage):
                        type = "resident-breeder"
                    else:
                        type = "non-resident-breeder" 
                else:
                    type="unknown-breeder"
            else:
                type = "unknown-breeder"                       
        except IndexError:
            type = "unknown-breeder"
        except ValueError:
            type = "unknown-breeder"
        return type	 
        
    def breeding_female_location_type(self):
        """This attribute defines whether a female's current location is the same as the breeding cage to which it belongs.

        This attribute is used to color breeding table entries such that male mice which are currently in a different cage can quickly be identified.
        The location is relative to the first breeding cage an animal is assigned to."""
        try:
            self.breeding_females.all()[0].Cage
            if self.breeding_females.all()[0].Cage is not None:
                if self.Cage is not None:
                    if self.breeding_males.all()[0].Cage == int(self.Cage):
                        type = "resident-breeder"
                    else:
                        type = "non-resident-breeder" 
                else:
                    type="unknown-breeder"
            else:
                type = "unknown-breeder"               
        except IndexError:
            type = "unknown-breeder"
        except ValueError:
            type = "unknown-breeder"            
        return type	         
      

    @models.permalink
    def get_absolute_url(self):
        return ('animal-detail', [str(self.id)])

    def save(self):
        """The save method for Animal class is over-ridden to set Alive=False when a Death date is entered.  This is not the case for a cause of death."""
        if self.Death:
            self.Alive = False
        super(Animal, self).save()

    class Meta:
        ordering = ['Born',]

class Breeding(models.Model):
    """This data model stores information about a particular breeding set

    A breeding set may contain one ore more males and females and must be defined via the progeny strain.  For example, in the case of generating a new strain, the strain indicates the new strain not the parental strains.  A breeding cage is defined as one male with one or more females.  If the breeding set is part of a timed mating experiment, then Timed_Mating must be selected.  Breeding cages are automatically inactivated upon saving when a End date is provided.  The only required field is Strain.  By default, querysets are ordered by Strain, then Start.
    """
    Females = models.ManyToManyField(Animal, blank=True, related_name="breeding_females")
    Male = models.ManyToManyField(Animal, related_name="breeding_males", blank=True) #should be males, but will have to check through the code to make sure this is ok to change
    Strain = models.ForeignKey(Strain, help_text="The strain of the pups")
    Cage = models.CommaSeparatedIntegerField(max_length=100,blank=True, null=True)
    BreedingName = models.CharField(max_length=50, blank=True, verbose_name="Breeding Set Name")
    Start = models.DateField(blank=True, null=True)
    End = models.DateField(blank=True, null=True)
    Crosstype = models.CharField(max_length=10, choices = CROSS_TYPE, blank=True)
    Notes = models.TextField(max_length=500, blank=True)
    Rack = models.CharField(max_length = 15, blank = True)
    Rack_Position = models.CharField(max_length = 15, blank = True, verbose_name="Rack Position") 
    Active = models.BooleanField(default=True)
    Timed_Mating = models.BooleanField(default=False, help_text="Is this cage a timed mating cage?")
    genotype = models.CharField(max_length = 15, choices = GENOTYPE_CHOICES, default = 'N.D.', help_text="The genotype of the pups (if known)")
    background = models.CharField(max_length = 25, choices = BACKGROUND_CHOICES, default="Mixed", help_text="The background of the pups")
    backcross = models.IntegerField(null=True, blank=True, help_text="Leave blank for mixed background.  This is the backcross of the pups.")
    generation = models.IntegerField(null=True, blank=True, help_text="The generation of the pups")

    def duration(self):
        """Calculates the breeding cage's duration.

        This is relative to the current date (if alive) or the date of inactivation (if not).
        The duration is formatted in days."""
        if self.End is not None:
            if self.Start is not None:
                age =  self.End - self.Start
            else:
                age = None
        else:
            if self.Start is not None:
                age =  datetime.date.today() - self.Start
            else:
                age = None
        if age is not None:
            return age.days 
        else:
            return "No Age"
    
    def __unicode__(self):
        return u'%s Breeding Cage: %s starting on %s'  %(self.Strain, self.Cage, self.Start)

    @models.permalink
    def get_absolute_url(self):
        return ('breeding-detail', [str(self.id)])

    def unweaned(self):
        """This attribute generates a queryset of unweaned animals for this breeding cage.  It is filtered for only Alive animals."""	
        return Animal.objects.filter(Breeding=self, Weaned__isnull=True, Alive=True)

    def male_breeding_location_type(self):
        """This attribute defines whether a breeding male's current location is the same as the breeding cage.

        This attribute is used to color breeding table entries such that male mice which are currently in a different cage can quickly be identified."""
        if int(self.Male.all()[0].Cage) == int(self.Cage):
            type = "resident breeder"
        else:
            type = "non-resident breeder"
        return type		

    def save(self):
        """The save function for a breeding cage has to automatic over-rides, Active and the Cage for the Breeder.
        
        In the case of Active, if an End field is specified, then the Active field is set to False.
        In the case of Cage, if a Cage is provided, and animals are specified under Male or Females for a Breeding object, then the Cage field for those animals is set to that of the breeding cage.  The same is true for both Rack and Rack Position."""
        if self.End:
            self.Active = False
        #if self.Cage:
        #    if self.Females:               
        #        for female_breeder in self.Females:
        #            female_breeder.Cage = self.Cage
        #            female_breeder.save()
        #    if self.Male:
        #        for male_breeder in self.Male:
        #            male_breeder.Cage = self.Cage
        #            male_breeder.save()
        super(Breeding, self).save()
        #if self.Rack:
        #    if self.Male:
        #        self.Male.Rack = self.Rack
        #        self.Male.save()
        #    if self.Females:
        #        if hasattr(self.Females, '__iter__') == True:     #This is required to determine of self.animals is a queryset or a single instance                     
        #            for female_breeder in self.Females:
        #                female_breeder.Rack = self.Rack
        #                female_breeder.save()
        #            else: 
        #                self.Females.Rack = self.Rack
        #                self.Females.save()
        #if self.Rack_Position:
        #    if self.male:
        #        self.male.Rack_Position = self.Rack_Position
        #        self.male.save()
        #    if self.females:
        #        if hasattr(self.females, '__iter__') == True:     #This is required to determine of self.animals is a queryset or a single instance                     
        #            for female_breeder in self.females:
        #                female_breeder.Rack_Position = self.Rack_Position
        #                female_breeder.save()
        #            else: 
        #                self.females.Rack_Position = self.Rack_Position
        #                self.females.save()
        #super(Breeding, self).save()
    class Meta:
        ordering = ['Strain', 'Start']
