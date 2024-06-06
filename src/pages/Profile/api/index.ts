import axios from 'axios';
import { toast } from 'react-toastify';

export interface UserProfileTypes {
  firstname: string;
  lastname: string;
  username: string;
  avatar: string;
}

export const fetchUserProfileData = async (username: string | undefined) => {
  try {
    // eslint-disable-next-line @typescript-eslint/restrict-template-expressions
    const res = await axios.get<UserProfileTypes>(`/api/accounts/profile/${username}/`);
    return res.data;
  } catch (err) {
    if (axios.isAxiosError(err) && err.response) {
      toast.error((err.response.data as { detail: string }).detail);
    }
  }
};
