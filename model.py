"""Model for Ubermelon shopping site."""

import sqlite3


class Melon(object):
    """An Ubermelon Melon type.

    A wrapper object that corresponds to rows in the melons table.
    """

    def __init__(self,
                 id,
                 melon_type,
                 common_name,
                 price, imgurl,
                 flesh_color,
                 rind_color,
                 seedless):
        self.id = id
        self.melon_type = melon_type
        self.common_name = common_name
        self.price = price
        self.imgurl = imgurl
        self.flesh_color = flesh_color
        self.rind_color = rind_color
        self.seedless = bool(seedless)

    def price_str(self):
        """Return price formatted as string $x.xx"""

        return "$%.2f" % self.price

    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return "<Melon: %s, %s, %s>" % (
            self.id, self.common_name, self.price_str())

    @classmethod
    def get_all(cls, max=30):
        """Return list of melons.

        Query the database for the first [max] melons, returning each as a
        Melon object
        """

        cursor = db_connect()
        QUERY = """
                  SELECT id,
                         melon_type,
                         common_name,
                         price,
                         imgurl,
                         flesh_color,
                         rind_color,
                         seedless
                   FROM Melons
                   WHERE imgurl <> ''
                   LIMIT ?;
               """

        cursor.execute(QUERY, (max,))
        melon_rows = cursor.fetchall()

        # list comprehension to build a list of Melon objects by going through
        # the database records and making a melon for each row. This is done
        # by unpacking in the for-loop.

        melons = [Melon(*row) for row in melon_rows]

        print melons

        return melons

    @classmethod
    def get_by_id(cls, id):
        """Query for a specific melon in the database by the primary key"""

        cursor = db_connect()
        QUERY = """
                  SELECT id,
                         melon_type,
                         common_name,
                         price,
                         imgurl,
                         flesh_color,
                         rind_color,
                         seedless
                   FROM Melons
                   WHERE id = ?;
               """

        cursor.execute(QUERY, (id,))

        row = cursor.fetchone()

        if not row:
            return None

        melon = Melon(*row)

        return melon


class Customer(object):
    """Ubermelon customer.

    A wrapper object that corresponds to rows in the customers table.
    """

    # TODO: need to implement this

    @classmethod
    def get_by_email(cls, email):
        """Query for a specific melon in the database by the primary key"""

        # TODO: Need to implement this.


def db_connect():
    """Return a database cursor."""

    conn = sqlite3.connect("melons.db")
    cursor = conn.cursor()
    return cursor

