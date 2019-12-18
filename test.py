import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
#from azure.iot.device import auth
from azure.iot.device import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult, IoTHubError


async def main():
    # Fetch the connection string from an enviornment variable
    conn_str = "HostName=VisualRecognitionHub.azure-devices.net;DeviceId=webcam-test;SharedAccessKey=uXnmYRt8SUkDbICRpsmwrxZQ5gzP8UD4gk4HC6f/ymc="

    # Create instance of the device client using the authentication provider
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    print("Sending message...")
    await device_client.send_message("{'message':'viva el paro nacional'}")
    print("Message successfully sent!")

    # finally, disconnect
    await device_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())