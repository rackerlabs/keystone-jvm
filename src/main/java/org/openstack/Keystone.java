package org.openstack;

import org.python.core.*;
import org.python.util.PythonInterpreter;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableAutoConfiguration
public class Keystone {
    public static void main(String []args) throws PyException {
        PythonInterpreter pythonInterpreter = new PythonInterpreter();
        pythonInterpreter.exec("from keystone_jvm.common import wsgi; wsgi.run()");
    }
}
