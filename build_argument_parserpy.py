from argparse import ArgumentParser

def build_parser():
    # name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
    # action - The basic type of action to be taken when this argument is encountered at the command line.
    # nargs - The number of command-line arguments that should be consumed.
    # const - A constant value required by some action and nargs selections.
    # default - The value produced if the argument is absent from the command line.
    # type - The type to which the command-line argument should be converted.
    # choices - A container of the allowable values for the argument.
    # required - Whether or not the command-line option may be omitted (optionals only).
    # help - A brief description of what the argument does.
    # metavar - A name for the argument in usage messages.
    # dest - The name of the attribute to be added to the object returned by parse_args().
    parser = ArgumentParser()
    parser.add_argument('--str_argument', type=str,
                        dest='str_argument', help='str argument',
                        metavar='STR_ARGUMENT', required=True)

    parser.add_argument('--bool_argument', dest='bool_argument', action='store_true',
                        help='action store true',
                        default=False)

    parser.add_argument('--int_argument', type=int,
                        dest='int_argument', help='int argument',
                        metavar='INT_ARGUMENT', default=1)

    parser.add_argument('--float_argument', type=float,
                        dest='float_argument',
                        help='float argument',
                        metavar='FLOAT_ARGUMENT', default=1.0)
    return parser.parse_args()


def main():
    arguments = build_parser()
    print(arguments)


if __name__ == '__main__':
    main()