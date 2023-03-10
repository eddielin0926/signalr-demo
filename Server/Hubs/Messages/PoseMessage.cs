namespace Server.Hubs.Messages
{
    public class PoseMessage
    {
        public PointMessage? Point;
        public QuaternionMessage? Quaternion;
        public PoseMessage(PointMessage? point, QuaternionMessage? quat)
        {
            Point = point;
            Quaternion = quat;
        }
    }
}
