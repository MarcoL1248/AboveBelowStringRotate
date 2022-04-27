# Run program with command:
# python TwoMethods.py


class TwoMethods:
    def __init__(self, n_list, comp_value, string, rotation):
        # Above below
        self.n_list = n_list
        self.comp_value = comp_value
        self.above_below_dict = {'above': 0, 'below': 0}

        # String rotation
        self.string = string
        self.rotation = rotation
        self.rotated_string = ''

    def get_above_below(self):
        for n in self.n_list:
            if n > self.comp_value:
                self.above_below_dict['above'] += 1
            elif n < self.comp_value:
                self.above_below_dict['below'] += 1
        print(self.above_below_dict)

    def rotate_string(self):
        if self.string == '':
            self.rotated_string = ''
        else:
            net_rotation = self.rotation % len(self.string)
            self.rotated_string = (2 * self.string)[len(self.string)-net_rotation: 2*len(self.string)-net_rotation]
        print(self.rotated_string)


if __name__ == '__main__':
    # Test case:
    num_list = [1, 5, 2, 1, 10]
    comparison_value = 6
    string_to_rotate = 'MyString'
    rotation_amount = 2
    obj = TwoMethods(num_list, comparison_value, string_to_rotate, rotation_amount)
    obj.get_above_below()
    obj.rotate_string()
