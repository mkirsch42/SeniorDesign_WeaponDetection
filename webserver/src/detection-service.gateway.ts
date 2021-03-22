import {
  SubscribeMessage,
  WebSocketGateway,
  OnGatewayInit,
  OnGatewayConnection,
  OnGatewayDisconnect,
  MessageBody,
} from '@nestjs/websockets';
import { Logger } from '@nestjs/common';
import { Socket, Server } from 'socket.io';

import { AppGateway } from './app.gateway';
import { DetectionDto } from './detection-dto';

@WebSocketGateway(3030)
export class DetectionServiceGateway
  implements OnGatewayInit, OnGatewayConnection, OnGatewayDisconnect {
  constructor(private appGateway: AppGateway) {}
  private readonly logger: Logger = new Logger(DetectionServiceGateway.name);

  @SubscribeMessage('detection')
  handleMessage(@MessageBody() detection: DetectionDto): void {
    this.appGateway.onDetection(detection);
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
