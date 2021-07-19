import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const x = new ClassRoom(19);
  const y = new ClassRoom(20);
  const z = new ClassRoom(34);
  return ([x, y, z]);
}
