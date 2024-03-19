

def main() :
    if () :
        m=True
    else:
        print("Use the parameter '-p' to change the inertia, ");
        print("/n"+"cognitive and social components.");
        print("Otherwise the default values will be: ");
        print("Inertia:             " + Swarm.DEFAULT_INERTIA);
        print("Cognitive Component: " + Swarm.DEFAULT_COGNITIVE);
        print("Social Component:    " + Swarm.DEFAULT_SOCIAL);
        m=False



def menu(flag):
    Swarm.swarm;
    Particle.FunctionType function;
    int particles, epochs;
    double inertia, cognitive, social;

    function = getFunction();
    particles = getUserInt("Particles: ");
    epochs = getUserInt("Epochs:    ");

    if (flag) :
        inertia = getUserDouble("Inertia:   ");
        cognitive = getUserDouble("Cognitive: ");
        social = getUserDouble("Social:    ");
        swarm =Swarm(function, particles, epochs, inertia, cognitive, social);
    else :
        swarm = Swarm(function, particles, epochs);



    swarm.run();


def getFunction():
    function = 0
    while(function == 0) :
        sc = input()
        printMenu()
        if (sc.hasNextInt()) :
            function = getFunction(sc.nextInt())
        else:
            print("Invalid input.")
    return function


def getUserInt ( msg):

        while (True):
            print(msg)

            if (hasNextInt()):
                input = nextInt()

                if (input <= 0) :
                    print("Number must be positive.");
                else:
                    break;

            else:
                print("Invalid input.")
        return input

    private static double getUserDouble (String msg) {
        double input;
        while (true) {
            Scanner sc = new Scanner(System.in);
            System.out.print(msg);

            if (sc.hasNextDouble()) {
                input = sc.nextDouble();

                if (input <= 0) {
                    System.out.println("Number must be positive.");
                } else {
                    break;
                }

            } else {
                System.out.println("Invalid input.");
            }
        }
        return input;
    }

    private static void printMenu () {
        System.out.println("----------------------------MENU----------------------------");
        System.out.println("Select a function:");
        System.out.println("1. (x^4)-2(x^3)");
        System.out.println("2. Ackley's Function");
        System.out.println("3. Booth's Function");
        System.out.println("4. Three Hump Camel Function");
        System.out.print("Function:  ");
    }

    private static Particle.FunctionType getFunction (int input) {
        if (input == 1)         return Particle.FunctionType.FunctionA;
        else if (input == 2)    return Particle.FunctionType.Ackleys;
        else if (input == 3)    return Particle.FunctionType.Booths;
        else if (input == 4)    return Particle.FunctionType.ThreeHumpCamel;
        System.out.println("Invalid Input.");
        return null;
    }

}