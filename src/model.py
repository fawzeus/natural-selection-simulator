from Creature import Creature
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers

# Define the Q-Network
class QNetwork(tf.keras.Model):
    def __init__(self, num_actions):
        super(QNetwork, self).__init__()
        self.layer1 = layers.Dense(64, activation='relu')
        self.layer2 = layers.Dense(64, activation='relu')
        self.output_layer = layers.Dense(num_actions, activation='linear')

    def call(self, state):
        x = self.layer1(state)
        x = self.layer2(x)
        return self.output_layer(x)

# Define the Deep Q-Network Agent
class DQNAgent:
    def __init__(self, num_actions):
        self.num_actions = num_actions
        self.q_network = QNetwork(num_actions)
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        self.gamma = 0.99  # Discount factor for future rewards

    def get_action(self, state):
        q_values = self.q_network(np.expand_dims(state, axis=0), training=False)
        action = np.squeeze(q_values.numpy())
        return action

    def train(self, state, action, reward, next_state, done):
        with tf.GradientTape() as tape:
            target = reward + self.gamma * np.max(self.q_network(np.expand_dims(next_state, axis=0), training=False))
            q_values = self.q_network(np.expand_dims(state, axis=0), training=True)
            action_index = np.arange(len(action))
            action_index = np.array([action_index])
            action_index = np.transpose(action_index)
            action_index = np.concatenate((action_index, np.expand_dims(action, axis=1)), axis=1)
            action_values = tf.gather_nd(q_values, action_index)
            loss = tf.keras.losses.mean_squared_error(target, action_values)

        grads = tape.gradient(loss, self.q_network.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.q_network.trainable_variables))


# Main training loop
num_actions = 1  # Assuming one continuous action for changing angle
num_episodes = 1000

agent = DQNAgent(num_actions)
creature = Creature()

for episode in range(num_episodes):
    state = creature.position  # Use position as a simple state representation

    # Get action from DQN
    action = agent.get_action(state)

    # Execute action and get new state
    creature.move(action)
    next_state = creature.position

    # Define a simple reward function (customize as needed)
    reward = 1.0 if np.random.rand() < 0.1 else 0.0  # Reward for finding food with a 10% chance

    # Train the DQN
    agent.train(state, action, reward, next_state, False)

    # Update state for the next iteration
    state = next_state

