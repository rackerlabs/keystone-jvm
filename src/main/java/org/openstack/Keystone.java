package org.openstack;

import org.python.util.PythonInterpreter;
import org.python.core.*;

public class Keystone {
    public static void main(String []args) throws PyException
    {
        PythonInterpreter pythonInterpreter = new PythonInterpreter();
        pythonInterpreter.exec("import wsgi; wsgi.run()");
    }
}
