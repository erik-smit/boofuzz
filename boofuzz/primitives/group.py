import six

from .base_primitive import BasePrimitive


class Group(BasePrimitive):
    def __init__(self, name, values, default_value=None, *args, **kwargs):
        """
        This primitive represents a list of static values, stepping through each one on mutation. You can tie a block
        to a group primitive to specify that the block should cycle through all possible mutations for *each* value
        within the group. The group primitive is useful for example for representing a list of valid opcodes.

        @type  name:            str
        @param name:            Name of group
        @type  values:          list or bytes
        @param values:          List of possible raw values this group can take.

        @param default_value:   Specifying a value when fuzzing() is complete
        """
        if default_value is None:
            default_value = values[0]
        super(Group, self).__init__(name, default_value, *args, **kwargs)

        self.values = values
        assert len(self.values) > 0, "You can't have an empty value list for your group!"
        for val in self.values:
            assert isinstance(val, (six.binary_type, six.string_types)), "Value list may only contain string/byte types"

    def mutations(self, default_value):
        for value in self.values:
            yield value

    def num_mutations(self, default_value):
        """
        Number of values in this primitive.

        @rtype:  int
        @return: Number of values in this primitive.
        :param default_value:
        """
        return len(self.values)
