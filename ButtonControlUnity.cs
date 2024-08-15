
using System.Collections;
using System.Collections.Generic;
using UnityEditor.Scripting.Python;
using UnityEngine;
using UnityEditor;

public class LeftRotate : MonoBehaviour
{
    public static void LeftRotateAction()
    {
        PythonRunner.RunString(@"
                import time;
                import paho.mqtt.client as paho;
                from paho import mqtt;

                client = paho.Client(client_id="""", userdata=None, protocol=paho.MQTTv5);

                client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS);
                client.username_pw_set(""elliot"", ""Elliot456"");
                client.connect(""90a408bbb7e64fdebaeefdd412a92c08.s1.eu.hivemq.cloud"", 8883);
                client.publish(""driver"", payload=""1"", qos=1);
                client.loop_start();
                client.loop_stop();
                ");
    }
}

