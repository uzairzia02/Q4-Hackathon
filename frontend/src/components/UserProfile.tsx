import React, { useState, useEffect } from 'react';
import clsx from 'clsx';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './UserProfile.module.css';

interface UserProfileData {
  hardware_tier: string;
  experience_level: string;
  learning_goals: string[];
}

interface UserProgress {
  [chapterId: string]: 'completed' | 'in_progress' | 'not_started';
}

const UserProfile: React.FC = () => {
  const {siteConfig} = useDocusaurusContext();
  const backendUrl = siteConfig.customFields?.backendUrl || 'http://localhost:8000'; // Replace with your backend URL
  const [profile, setProfile] = useState<UserProfileData | null>(null);
  const [progress, setProgress] = useState<UserProgress | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Placeholder for user ID and token - in a real app, these would come from authentication context
  const userId = 'testuser';
  const authToken = 'your_jwt_token'; // Replace with actual JWT token

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        setLoading(true);
        const response = await fetch(`${backendUrl}/users/${userId}/profile`, {
          headers: {
            'Authorization': `Bearer ${authToken}`,
            'Content-Type': 'application/json',
          },
        });
        if (!response.ok) {
          throw new Error(`Error fetching profile: ${response.statusText}`);
        }
        const data: UserProfileData = await response.json();
        setProfile(data);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    if (userId && authToken) {
      fetchUserProfile();
    } else {
      setLoading(false);
      setError("User not logged in or token missing.");
    }
  }, [userId, authToken, backendUrl]);

  const updateProfile = async () => {
    if (!profile) return;
    try {
      setLoading(true);
      const response = await fetch(`${backendUrl}/users/${userId}/profile`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${authToken}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(profile),
      });
      if (!response.ok) {
        throw new Error(`Error updating profile: ${response.statusText}`);
      }
      alert('Profile updated successfully!');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading profile...</div>;
  if (error) return <div className={styles.error}>Error: {error}</div>;
  if (!profile) return <div>No profile data available.</div>;

  return (
    <div className={styles.profileCard}>
      <h2>Your Learning Profile</h2>
      <p><strong>User ID:</strong> {userId}</p>
      <div>
        <label>Hardware Tier:</label>
        <input
          type="text"
          value={profile.hardware_tier}
          onChange={(e) => setProfile({ ...profile, hardware_tier: e.target.value })}
        />
      </div>
      <div>
        <label>Experience Level:</label>
        <input
          type="text"
          value={profile.experience_level}
          onChange={(e) => setProfile({ ...profile, experience_level: e.target.value })}
        />
      </div>
      <div>
        <label>Learning Goals (comma separated):</label>
        <input
          type="text"
          value={profile.learning_goals.join(', ')}
          onChange={(e) => setProfile({ ...profile, learning_goals: e.target.value.split(',').map(s => s.trim()) })}
        />
      </div>
      <button onClick={updateProfile}>Save Profile</button>

      <h3>Reading Progress (Placeholder)</h3>
      <p>This section would display your chapter completion status and personalized recommendations.</p>
      {/* Example: Display progress for some chapters */}
      <ul>
        <li>Intro to ROS 2: {progress?.['intro-ros2'] || 'Not Started'}</li>
        <li>Gazebo Simulation: {progress?.['gazebo-sim'] || 'Not Started'}</li>
      </ul>
    </div>
  );
};

export default UserProfile;
