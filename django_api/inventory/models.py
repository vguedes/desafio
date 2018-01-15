from django.db import models


class Country(models.Model):
    """Model definition for Country."""

    name = models.CharField(max_length=254)

    class Meta:
        """Meta definition for Country."""

        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        """Unicode representation of Country."""
        return self.name


class State(models.Model):
    """Model definition for State."""

    country = models.ForeignKey(Country, on_delete='cascade')
    name = models.CharField(max_length=254)

    class Meta:
        """Meta definition for State."""

        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        """Unicode representation of State."""
        return "{0} of {1!s}".format(self.name, self.country)


class City(models.Model):
    """Model definition for City."""

    state = models.ForeignKey(State, on_delete='cascade')
    name = models.CharField(max_length=254)

    class Meta:
        """Meta definition for City."""

        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        """Unicode representation of City."""
        return "{0} of {1!s} of {2!s}".format(
            self.name,
            self.state.name,
            self.state.country.name
        )


class Consumer(models.Model):
    """Model definition for Consumer."""

    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    class Meta:
        """Meta definition for Consumer."""

        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'

    def __str__(self):
        """Unicode representation of Consumer."""
        return self.name



class Company(models.Model):
    """Model definition for Company."""

    city = models.ForeignKey(City, on_delete='cascade')
    name = models.CharField(max_length=254)

    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        """Unicode representation of Company."""
        return self.name

class Complain(models.Model):
    """Model definition for Complain."""

    consumer = models.ForeignKey(Consumer, on_delete='cascade')
    city = models.ForeignKey(City, on_delete='cascade')
    company = models.ForeignKey(Company, on_delete='cascade')
    title = models.CharField(max_length=254)
    description = models.TextField()

    @property
    def ellipsed_title(self):
        return (
            len(self.title) >= 20 and
            '{}...'.format(self.title[:20].strip()) or
            self.title
        )

    @property
    def ellipsed_description(self):
        return (
            len(self.description) >= 100 and
            '{}...'.format(self.description[:100].strip()) or
            self.description
        )

    class Meta:
        """Meta definition for Complain."""

        verbose_name = 'Complain'
        verbose_name_plural = 'Complains'

    def __str__(self):
        """Unicode representation of Complain."""
        return "{0} of {1!s}".format(
            self.ellipsed_title,
            self.company
        )

