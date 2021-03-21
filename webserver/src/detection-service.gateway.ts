import {
  SubscribeMessage,
  WebSocketGateway,
  OnGatewayInit,
  WebSocketServer,
  OnGatewayConnection,
  OnGatewayDisconnect,
} from '@nestjs/websockets';
import { Logger } from '@nestjs/common';
import { Socket, Server } from 'socket.io';

import { AppGateway } from './app.gateway'

@WebSocketGateway(3030)
export class DetectionServiceGateway
  implements OnGatewayInit, OnGatewayConnection, OnGatewayDisconnect {
    constructor(private server: Server) {}
    private readonly logger: Logger = new Logger(DetectionServiceGateway.name);
  
    @SubscribeMessage('detection')
    handleMessage(client: Socket, payload: string, appGateway: AppGateway): void {
      appGateway.onDetection(JSON.parse(payload));
    }
  
    afterInit(server: Server) {
      this.logger.log('Init');
    }
  
    handleDisconnect(client: Socket) {
      this.logger.log(`Client disconnected: ${client.id}`);
    }
  
    handleConnection(client: Socket, ...args: any[]) {
      this.logger.log(`Client connected: ${client.id}`);
    }
}
