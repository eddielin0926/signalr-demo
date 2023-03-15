namespace Server.Hubs.Messages
{
    public class PoseMessage
    {
        public PointMessage? Point { get; set; }
        public QuaternionMessage? Quaternion { get; set; }
        public PoseMessage(PointMessage? point, QuaternionMessage? quat)
        {
            Point = point;
            Quaternion = quat;
        }
    }
}
